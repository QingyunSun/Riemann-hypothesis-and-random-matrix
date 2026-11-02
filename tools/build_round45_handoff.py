"""Assemble the detailed Rounds 4-5 supplement from pinned public proof reports."""
from pathlib import Path
import hashlib
import json
import re

from build_handoff import cleaned

ROOT = Path(__file__).resolve().parents[1]
PIN = "c74b326afb90b79d16ce480b183111e0d5f7daf6"
WEB = f"https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/{PIN}/"
REPORTS = [
    "research/reports/prime186_round4.md",
    "research/prime-gaps/round4/prime-credit/prime_alpha_credit.md",
    "research/prime-gaps/round4/restoration-proof/ALPHA_RECTANGLE_INDEPENDENT_REVIEW.md",
    "research/prime-gaps/round4/restoration-proof/RESTORATION_PROOF_AUDIT.md",
    "research/prime-gaps/round4/k39-trial/REPORT.md",
    "research/prime-gaps/round4/repro-flint/README.md",
    "research/reports/prime186_round5.md",
    "research/prime-gaps/round5/exceptional-radius/EXCEPTIONAL_RADIUS_EXTENSION.md",
    "research/prime-gaps/round5/geometry-audit/GEOMETRY_SOURCE_AUDIT.md",
    "research/prime-gaps/round5/geometry-trial/REPORT.md",
]


def main():
    parts = ["""# 第 4-5 轮详细研究补编

本补编接续 333 页公开交接档案（检查点 055a4a0），保留随后两轮的完整证明报告和审查记录。资料源检查点为 c74b326。此前的 ACUE、零点热流、算术相关性、反例与历史路线仍应连同主档案阅读。

本轮严格结果是：同一 k=40 筛法的新增正项使已发表基线上的证明余量从 23.36045 ppm 增至 24.86626 ppm；素数间隙结论仍为 186。另有变量半径异常平方估计、足够的支撑几何条件、一个网格修复，以及完整保存的 k=39 负向搜索。没有证明 RH、Alternative Hypothesis 的反驳、新的 zeta 半间隙结果或低于 186 的素数间隙。

正文区分普通数学证明、独立内部审查、精确有理数证书、浮点计算、原论文输入和未完成义务。普通证明及内部审查尚不等于 Lean 形式验证或外部同行评审。53 项平方积分逐项区间、矩阵、参数、执行日志和哈希清单另存于仓库，不把大型数组印成难以核查的页面。

第 5 轮综合报告澄清原搜索报告的数值最大误差范围：较小的最大值只对应 12 个完整 77 维候选；仓库另存的截断候选有不同的全矩阵残差。所有 36 个向量均经过集成核查。

为便于机器和人工追溯，每篇报告列出原路径和 SHA256，文内相对链接指向该固定 Git 提交。报告文字及数学内容保留；只调整标题层级、链接、过长公式的换行，并补齐原始数据表缺少的 Markdown 表头分隔线。原文中关于暂缓、下一步或代理的描述属于研究记录。

## 接手顺序

先读两轮综合报告，接着审查新增正项及其独立证明，再查看完整 k=39 搜索的缺口。变量半径估计与几何条件可以作为后续新支撑的输入，但不能替代新的失败覆盖及物理积分证书。避免重复相同端点扫描；寻找能改变当前缺口的产品权重、可证明支撑或算术混合项。
"""]
    index = []
    for i, rel in enumerate(REPORTS, 1):
        source = ROOT / rel
        raw = source.read_text()
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        def link(match):
            target = match[1]
            if "://" in target or target.startswith("#"):
                return match[0]
            absolute = (source.parent / target).resolve()
            if absolute.exists() and absolute.is_relative_to(ROOT):
                return "](" + WEB + absolute.relative_to(ROOT).as_posix() + ")"
            return match[0]
        display = raw.replace(
            r"""a=1.0166236774089747\ldots,
\quad A=1.0449558074337872\ldots,
\quad L=0.5498119373071242\ldots,
\quad \xi=0.028332320501728507\ldots.""",
            r"""\begin{aligned}
a&=1.0166236774089747\ldots,& A&=1.0449558074337872\ldots,\\
L&=0.5498119373071242\ldots,& \xi&=0.028332320501728507\ldots.
\end{aligned}""")
        display = display.replace(
            "| tag | physical r | plateau | K | grid | rho_star Jcap/I |\n",
            "| tag | physical r | plateau | K | grid | rho_star Jcap/I |\n|---|---:|---|---:|---:|---:|\n")
        if source.name == "EXCEPTIONAL_RADIUS_EXTENSION.md":
            # Bare stars in prose otherwise open long Markdown emphasis spans.
            display = re.sub(r"(?<![\\\w])(xi|rho)_\*", lambda m: {"xi": r"\(\xi_*\)", "rho": r"\(\rho_*\)"}[m[1]], display)
        content = cleaned(re.sub(r"\]\(([^)]+)\)", link, display))
        parts.append(f"# Current report {i:02d}: {source.stem}\n\nSource: [{rel}]({WEB}{rel}). SHA256: `{digest}`.\n\n" + content)
        index.append({"path": rel, "sha256": digest, "bytes": source.stat().st_size})
    output = ROOT / "docs/handoff/ASTRA_ROUNDS_4_5_HANDOFF.md"
    output.write_text("\n\n".join(parts) + "\n")
    output.with_name("ROUNDS_4_5_ARCHIVE_INDEX.json").write_text(json.dumps({"source_commit": PIN, "reports": index}, indent=2) + "\n")
    print(json.dumps({"reports": len(index), "bytes": output.stat().st_size, "output": str(output)}))


if __name__ == "__main__":
    main()
