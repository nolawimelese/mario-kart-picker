import React from "react";
import { Icon } from "../brand/Icon";
import type { IconName } from "../brand/Icon";

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "ghost" | "outline" | "danger";
  size?: "sm" | "md" | "lg";
  /** Icon name shown before the label. */
  iconLeft?: IconName;
  /** Icon name shown after the label. */
  iconRight?: IconName;
  /** Full-width block button. */
  block?: boolean;
}

/**
 * MK Picker Button — chunky arcade control with a hard "pop" shadow that
 * depresses on press. Variants: primary, secondary, ghost, outline, danger.
 */
export function Button({
  children,
  variant = "primary",
  size = "md",
  iconLeft,
  iconRight,
  block = false,
  disabled = false,
  type = "button",
  style,
  ...rest
}: ButtonProps) {
  const sizes = {
    sm: { h: "var(--control-h-sm)", px: 14, fs: "var(--text-sm)", icon: 16, gap: 6 },
    md: { h: "var(--control-h-md)", px: 18, fs: "var(--text-md)", icon: 18, gap: 8 },
    lg: { h: "var(--control-h-lg)", px: 24, fs: "var(--text-lg)", icon: 22, gap: 10 },
  };
  const s = sizes[size] || sizes.md;

  const palettes = {
    primary:   { bg: "var(--boost-500)", fg: "#fff", bd: "var(--ink-900)", pop: true },
    secondary: { bg: "var(--drift-500)", fg: "#fff", bd: "var(--ink-900)", pop: true },
    danger:    { bg: "var(--shell-red)", fg: "#fff", bd: "var(--ink-900)", pop: true },
    outline:   { bg: "var(--white)", fg: "var(--ink-900)", bd: "var(--ink-900)", pop: true },
    ghost:     { bg: "transparent", fg: "var(--ink-700)", bd: "transparent", pop: false },
  };
  const p = palettes[variant] || palettes.primary;

  const base: React.CSSProperties = {
    display: block ? "flex" : "inline-flex",
    width: block ? "100%" : undefined,
    alignItems: "center",
    justifyContent: "center",
    gap: s.gap,
    height: s.h,
    padding: `0 ${s.px}px`,
    fontFamily: "var(--font-ui)",
    fontWeight: "var(--weight-semibold)",
    fontSize: s.fs,
    lineHeight: 1,
    color: p.fg,
    background: p.bg,
    border: `var(--border-base) solid ${p.bd}`,
    borderRadius: "var(--radius-pill)",
    cursor: disabled ? "not-allowed" : "pointer",
    opacity: disabled ? 0.5 : 1,
    boxShadow: p.pop ? "var(--shadow-pop-sm)" : "none",
    transition: "transform var(--dur-fast) var(--ease-snap), box-shadow var(--dur-fast) var(--ease-snap), background var(--dur-fast)",
    WebkitTapHighlightColor: "transparent",
    userSelect: "none",
    whiteSpace: "nowrap",
    ...style,
  };

  const interactive = !disabled && p.pop;
  const onDown = (e: React.MouseEvent<HTMLButtonElement>) => { if (interactive) { e.currentTarget.style.transform = "translate(2px,2px)"; e.currentTarget.style.boxShadow = "0 0 0 var(--ink-900)"; } };
  const onUp = (e: React.MouseEvent<HTMLButtonElement>) => { if (interactive) { e.currentTarget.style.transform = ""; e.currentTarget.style.boxShadow = "var(--shadow-pop-sm)"; } };
  const onEnterGhost = (e: React.MouseEvent<HTMLButtonElement>) => { if (!disabled && variant === "ghost") e.currentTarget.style.background = "var(--ink-100)"; };
  const onLeaveGhost = (e: React.MouseEvent<HTMLButtonElement>) => { if (variant === "ghost") e.currentTarget.style.background = "transparent"; onUp(e); };

  return (
    <button
      type={type}
      disabled={disabled}
      style={base}
      onMouseDown={onDown}
      onMouseUp={onUp}
      onMouseEnter={onEnterGhost}
      onMouseLeave={onLeaveGhost}
      {...rest}
    >
      {iconLeft && <Icon name={iconLeft} size={s.icon} />}
      {children}
      {iconRight && <Icon name={iconRight} size={s.icon} />}
    </button>
  );
}
