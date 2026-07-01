import React from "react";
import { Icon } from "../brand/Icon";
import type { IconName } from "../brand/Icon";

export interface ToastProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "title"> {
  tone?: "success" | "boost" | "info" | "danger" | "coin";
  title?: React.ReactNode;
  message?: React.ReactNode;
  /** Override the auto icon. */
  icon?: IconName;
  onClose?: () => void;
}

/** Toast / inline notification. Left accent stripe + icon by tone. */
export function Toast({ tone = "success", title, message, onClose, icon, style, ...rest }: ToastProps) {
  const tones: Record<string, { c: string; i: IconName }> = {
    success: { c: "var(--mushroom)", i: "check-circle" },
    boost: { c: "var(--boost-500)", i: "zap" },
    info: { c: "var(--drift-500)", i: "info" },
    danger: { c: "var(--shell-red)", i: "alert" },
    coin: { c: "var(--coin-500)", i: "trophy" },
  };
  const t = tones[tone] || tones.info;
  return (
    <div
      role="status"
      style={{
        display: "flex",
        alignItems: "flex-start",
        gap: 12,
        width: 340,
        maxWidth: "100%",
        padding: "14px 14px 14px 16px",
        background: "var(--white)",
        borderRadius: "var(--radius-md)",
        border: "var(--border-base) solid var(--ink-900)",
        boxShadow: "var(--shadow-pop)",
        borderLeft: `6px solid ${t.c}`,
        ...style,
      }}
      {...rest}
    >
      <span style={{ color: t.c, marginTop: 1 }}>
        <Icon name={icon || t.i} size={20} />
      </span>
      <div style={{ flex: 1, minWidth: 0 }}>
        {title && <div style={{ fontFamily: "var(--font-ui)", fontWeight: 700, fontSize: "var(--text-md)", color: "var(--ink-900)" }}>{title}</div>}
        {message && <div style={{ fontFamily: "var(--font-body)", fontWeight: 600, fontSize: "var(--text-sm)", color: "var(--ink-500)", marginTop: 2 }}>{message}</div>}
      </div>
      {onClose && (
        <button type="button" onClick={onClose} aria-label="Dismiss" style={{
          display: "grid", placeItems: "center", width: 24, height: 24, cursor: "pointer",
          background: "transparent", border: "none", color: "var(--ink-400)", flexShrink: 0,
        }}>
          <Icon name="x" size={16} />
        </button>
      )}
    </div>
  );
}
