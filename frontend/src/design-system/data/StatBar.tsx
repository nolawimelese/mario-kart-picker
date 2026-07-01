import React from "react";
import { Icon } from "../brand/Icon";
import type { IconName } from "../brand/Icon";

export interface StatBarProps extends React.HTMLAttributes<HTMLDivElement> {
  label?: string;
  value?: number;
  max?: number;
  /** Fill color (CSS value). Default boost. */
  color?: string;
  icon?: IconName;
  /** Number of pip segments to overlay (0 = smooth). */
  segments?: number;
}

/**
 * StatBar — a labeled attribute meter (0–100). Used across track cards for
 * stats like Speed, Chaos, Shortcut potential. Segmented "pip" style track.
 */
export function StatBar({ label, value = 0, max = 100, color = "var(--boost-500)", icon, segments = 0, style, ...rest }: StatBarProps) {
  const pct = Math.max(0, Math.min(100, (value / max) * 100));
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 6, ...style }} {...rest}>
      {label && (
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <span style={{
            display: "inline-flex", alignItems: "center", gap: 5,
            fontFamily: "var(--font-ui)",
            fontWeight: "var(--weight-semibold)",
            fontSize: "var(--text-xs)",
            letterSpacing: "var(--tracking-caps)",
            textTransform: "uppercase",
            color: "var(--ink-500)",
          }}>
            {icon && <Icon name={icon} size={13} color="var(--ink-400)" />}
            {label}
          </span>
          <span style={{
            fontFamily: "var(--font-mono)",
            fontSize: "var(--text-xs)",
            fontWeight: 700,
            color: "var(--ink-700)",
          }}>{Math.round(value)}</span>
        </div>
      )}
      <div style={{
        position: "relative",
        height: 12,
        borderRadius: "var(--radius-pill)",
        background: "var(--ink-100)",
        border: "var(--border-base) solid var(--ink-900)",
        overflow: "hidden",
      }}>
        <div style={{
          position: "absolute",
          inset: 0,
          width: `${pct}%`,
          background: color,
          borderRadius: "var(--radius-pill)",
          transition: "width var(--dur-slow) var(--ease-out)",
          ...(segments ? {
            backgroundImage: "repeating-linear-gradient(90deg, rgba(0,0,0,0.18) 0 2px, transparent 2px var(--seg))",
            ["--seg"]: `${100 / segments}%`,
          } as React.CSSProperties : {}),
        }} />
      </div>
    </div>
  );
}
