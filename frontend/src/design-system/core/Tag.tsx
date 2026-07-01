import React from "react";
import { Icon } from "../brand/Icon";
import type { IconName } from "../brand/Icon";

export interface TagProps extends React.HTMLAttributes<HTMLSpanElement> {
  icon?: IconName;
  /** Selected (boost outline) state — for filter chips. */
  selected?: boolean;
  /** Show a remove (x) affordance. */
  removable?: boolean;
  onRemove?: (e: React.MouseEvent) => void;
}

/**
 * Tag / filter chip. Selectable (toggles a boost outline) and optionally
 * removable. Used heavily across the track filters.
 */
export function Tag({ children, icon, selected = false, removable = false, onRemove, onClick, style, ...rest }: TagProps) {
  return (
    <span
      onClick={onClick}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 6,
        height: 32,
        padding: removable ? "0 6px 0 12px" : "0 14px",
        fontFamily: "var(--font-ui)",
        fontWeight: "var(--weight-medium)",
        fontSize: "var(--text-sm)",
        lineHeight: 1,
        cursor: onClick ? "pointer" : "default",
        color: selected ? "var(--boost-600)" : "var(--ink-700)",
        background: selected ? "var(--boost-50)" : "var(--white)",
        border: `var(--border-base) solid ${selected ? "var(--boost-500)" : "var(--ink-200)"}`,
        borderRadius: "var(--radius-pill)",
        transition: "background var(--dur-fast), border-color var(--dur-fast), color var(--dur-fast)",
        userSelect: "none",
        ...style,
      }}
      {...rest}
    >
      {icon && <Icon name={icon} size={15} />}
      {children}
      {removable && (
        <span
          role="button"
          aria-label="Remove"
          onClick={(e) => { e.stopPropagation(); onRemove && onRemove(e); }}
          style={{
            display: "inline-grid",
            placeItems: "center",
            width: 20,
            height: 20,
            borderRadius: 999,
            background: selected ? "var(--boost-100)" : "var(--ink-100)",
            cursor: "pointer",
          }}
        >
          <Icon name="x" size={13} />
        </span>
      )}
    </span>
  );
}
