import React from "react";
import { Icon } from "../brand/Icon";
import type { IconName } from "../brand/Icon";

export interface DialogProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "title"> {
  open?: boolean;
  onClose?: () => void;
  title?: React.ReactNode;
  icon?: IconName;
  /** Footer actions (e.g. Button elements). */
  footer?: React.ReactNode;
  width?: number;
}

/** Modal dialog with a chunky arcade card and dimmed backdrop. */
export function Dialog({ open = true, onClose, title, icon, children, footer, width = 460, style, onClick, ...rest }: DialogProps) {
  const cardRef = React.useRef<HTMLDivElement>(null);
  const titleId = React.useId();

  React.useEffect(() => {
    if (!open) return;
    cardRef.current?.focus();
    const onKey = (e: KeyboardEvent) => { if (e.key === "Escape") onClose?.(); };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [open, onClose]);

  if (!open) return null;
  return (
    <div
      onClick={onClose}
      style={{
        position: "fixed",
        inset: 0,
        background: "rgba(22,19,32,0.45)",
        backdropFilter: "blur(2px)",
        display: "grid",
        placeItems: "center",
        padding: 24,
        zIndex: 1000,
      }}
    >
      <div
        ref={cardRef}
        onClick={(e) => { e.stopPropagation(); onClick?.(e); }}
        role="dialog"
        aria-modal="true"
        aria-labelledby={title ? titleId : undefined}
        tabIndex={-1}
        style={{
          width,
          maxWidth: "100%",
          background: "var(--white)",
          borderRadius: "var(--radius-lg)",
          border: "var(--border-chunky) solid var(--ink-900)",
          boxShadow: "var(--shadow-pop-lg)",
          overflow: "hidden",
          outline: "none",
          ...style,
        }}
        {...rest}
      >
        <div style={{
          display: "flex",
          alignItems: "center",
          gap: 12,
          padding: "18px 20px",
          borderBottom: "var(--border-base) solid var(--ink-100)",
        }}>
          {icon && (
            <span style={{
              display: "grid", placeItems: "center", width: 36, height: 36,
              borderRadius: "var(--radius-sm)", background: "var(--boost-100)", color: "var(--boost-600)",
            }}>
              <Icon name={icon} size={20} />
            </span>
          )}
          <h4 id={titleId} style={{ flex: 1, margin: 0, fontSize: "var(--text-xl)" }}>{title}</h4>
          {onClose && (
            <button type="button" onClick={onClose} aria-label="Close" style={{
              display: "grid", placeItems: "center", width: 32, height: 32, cursor: "pointer",
              background: "transparent", border: "none", borderRadius: "var(--radius-xs)", color: "var(--ink-500)",
            }}>
              <Icon name="x" size={20} />
            </button>
          )}
        </div>
        <div style={{ padding: 20, fontFamily: "var(--font-body)", color: "var(--text-body)", fontWeight: 600 }}>
          {children}
        </div>
        {footer && (
          <div style={{
            display: "flex", justifyContent: "flex-end", gap: 10, padding: "16px 20px",
            borderTop: "var(--border-base) solid var(--ink-100)", background: "var(--ink-50)",
          }}>
            {footer}
          </div>
        )}
      </div>
    </div>
  );
}
