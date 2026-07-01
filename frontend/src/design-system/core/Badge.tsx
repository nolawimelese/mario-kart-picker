import React from "react";

export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  color?: "boost" | "drift" | "coin" | "success" | "danger" | "purple" | "neutral";
  /** Soft tinted fill instead of solid. */
  soft?: boolean;
  /** Show a leading status dot. */
  dot?: boolean;
}

/** Small status/label badge. Solid or soft fill across the semantic palette. */
export function Badge({ children, color = "boost", soft = false, dot = false, style, ...rest }: BadgeProps) {
  const map = {
    boost: ["var(--boost-500)", "var(--boost-100)", "var(--boost-600)"],
    drift: ["var(--drift-500)", "var(--drift-100)", "var(--drift-600)"],
    coin: ["var(--coin-500)", "var(--coin-100)", "#8a6a00"],
    success: ["var(--mushroom)", "#d6f7e4", "#0e8f48"],
    danger: ["var(--shell-red)", "#ffe0e6", "#d61f3f"],
    purple: ["var(--star-purple)", "#ece4ff", "#6d39e0"],
    neutral: ["var(--ink-600)", "var(--ink-100)", "var(--ink-700)"],
  };
  const [solid, softBg, softFg] = map[color] || map.boost;
  const isSoftCoin = color === "coin";

  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 5,
        height: 22,
        padding: "0 9px",
        fontFamily: "var(--font-ui)",
        fontWeight: "var(--weight-semibold)",
        fontSize: "var(--text-xs)",
        letterSpacing: "0.01em",
        lineHeight: 1,
        borderRadius: "var(--radius-pill)",
        color: soft ? softFg : isSoftCoin ? "var(--ink-900)" : "#fff",
        background: soft ? softBg : solid,
        border: soft ? "1px solid transparent" : "none",
        ...style,
      }}
      {...rest}
    >
      {dot && (
        <span style={{ width: 6, height: 6, borderRadius: 999, background: soft ? solid : "currentColor" }} />
      )}
      {children}
    </span>
  );
}
