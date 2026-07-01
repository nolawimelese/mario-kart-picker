import React from "react";

export interface TierBadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** Tier letter — S, A, B, C, D or F. */
  tier?: "S" | "A" | "B" | "C" | "D" | "F" | string;
  size?: "sm" | "md" | "lg";
}

/**
 * TierBadge — the signature ranking chip (S / A / B / C / D / F).
 * Each tier has a fixed brand color. Used in tier lists and on track cards.
 */
const TIERS: Record<string, string> = {
  S: "var(--tier-s)",
  A: "var(--tier-a)",
  B: "var(--tier-b)",
  C: "var(--tier-c)",
  D: "var(--tier-d)",
  F: "var(--tier-f)",
};

export function TierBadge({ tier = "S", size = "md", style, ...rest }: TierBadgeProps) {
  const t = String(tier).toUpperCase();
  const bg = TIERS[t] || "var(--ink-400)";
  const dims = { sm: 28, md: 38, lg: 52 };
  const fs = { sm: 16, md: 22, lg: 30 };
  const dim = dims[size] || dims.md;
  const lightTiers = t === "B" || t === "C";
  return (
    <span
      style={{
        display: "inline-grid",
        placeItems: "center",
        width: dim,
        height: dim,
        background: bg,
        color: lightTiers ? "var(--ink-900)" : "#fff",
        fontFamily: "var(--font-display)",
        fontSize: fs[size] || 22,
        lineHeight: 1,
        paddingTop: dim * 0.06,
        borderRadius: "var(--radius-sm)",
        border: "var(--border-base) solid var(--ink-900)",
        boxShadow: "var(--shadow-pop-sm)",
        ...style,
      }}
      {...rest}
    >
      {t}
    </span>
  );
}
