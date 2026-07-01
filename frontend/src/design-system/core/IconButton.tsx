import React from "react";
import { Icon } from "../brand/Icon";
import type { IconName } from "../brand/Icon";

export interface IconButtonProps extends Omit<React.ButtonHTMLAttributes<HTMLButtonElement>, "size"> {
  icon: IconName;
  variant?: "primary" | "secondary" | "outline" | "ghost";
  size?: "sm" | "md" | "lg";
  /** Pill-round instead of rounded-square. */
  round?: boolean;
  /** Accessible label (also used as title tooltip). */
  label?: string;
}

/** Square/round icon-only button. Same arcade feel as Button. */
export function IconButton({
  icon,
  variant = "outline",
  size = "md",
  round = false,
  disabled = false,
  label,
  style,
  ...rest
}: IconButtonProps) {
  const sizes = { sm: 34, md: 42, lg: 52 };
  const iconSizes = { sm: 18, md: 20, lg: 24 };
  const dim = sizes[size] || sizes.md;

  const palettes = {
    primary: { bg: "var(--boost-500)", fg: "#fff", bd: "var(--ink-900)", pop: true },
    secondary: { bg: "var(--drift-500)", fg: "#fff", bd: "var(--ink-900)", pop: true },
    outline: { bg: "var(--white)", fg: "var(--ink-900)", bd: "var(--ink-900)", pop: true },
    ghost: { bg: "transparent", fg: "var(--ink-600)", bd: "transparent", pop: false },
  };
  const p = palettes[variant] || palettes.outline;
  const interactive = !disabled && p.pop;

  return (
    <button
      type="button"
      aria-label={label}
      title={label}
      disabled={disabled}
      onMouseDown={(e) => { if (interactive) { e.currentTarget.style.transform = "translate(2px,2px)"; e.currentTarget.style.boxShadow = "0 0 0 var(--ink-900)"; } }}
      onMouseUp={(e) => { if (interactive) { e.currentTarget.style.transform = ""; e.currentTarget.style.boxShadow = "var(--shadow-pop-sm)"; } }}
      onMouseLeave={(e) => { if (interactive) { e.currentTarget.style.transform = ""; e.currentTarget.style.boxShadow = "var(--shadow-pop-sm)"; } if (variant === "ghost") e.currentTarget.style.background = "transparent"; }}
      onMouseEnter={(e) => { if (!disabled && variant === "ghost") e.currentTarget.style.background = "var(--ink-100)"; }}
      style={{
        display: "inline-grid",
        placeItems: "center",
        width: dim,
        height: dim,
        color: p.fg,
        background: p.bg,
        border: `var(--border-base) solid ${p.bd}`,
        borderRadius: round ? "var(--radius-pill)" : "var(--radius-sm)",
        cursor: disabled ? "not-allowed" : "pointer",
        opacity: disabled ? 0.5 : 1,
        boxShadow: p.pop ? "var(--shadow-pop-sm)" : "none",
        transition: "transform var(--dur-fast) var(--ease-snap), box-shadow var(--dur-fast) var(--ease-snap), background var(--dur-fast)",
        WebkitTapHighlightColor: "transparent",
        ...style,
      }}
      {...rest}
    >
      <Icon name={icon} size={iconSizes[size] || 20} />
    </button>
  );
}
