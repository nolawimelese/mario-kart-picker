import React from "react";

export interface AvatarProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** Player name — used for initials when no image. */
  name?: string;
  /** Image URL. */
  src?: string;
  /** Diameter in px. Default 40. */
  size?: number;
  /** Background color for the initials variant. */
  color?: string;
  /** Show an online/active ring. */
  ring?: boolean;
}

/** Avatar — round player chip with image or initials, optional online ring. */
export function Avatar({ name = "", src, size = 40, color = "var(--star-purple)", ring = false, style, ...rest }: AvatarProps) {
  const initials = name
    .split(" ")
    .map((w) => w[0])
    .filter(Boolean)
    .slice(0, 2)
    .join("")
    .toUpperCase();
  return (
    <span
      style={{
        display: "inline-grid",
        placeItems: "center",
        width: size,
        height: size,
        borderRadius: "var(--radius-pill)",
        background: src ? "transparent" : color,
        color: "#fff",
        fontFamily: "var(--font-ui)",
        fontWeight: "var(--weight-bold)",
        fontSize: size * 0.4,
        overflow: "hidden",
        border: "var(--border-base) solid var(--ink-900)",
        boxShadow: ring ? "0 0 0 2px var(--white), 0 0 0 4px var(--mushroom)" : "none",
        flexShrink: 0,
        ...style,
      }}
      {...rest}
    >
      {src ? (
        <img src={src} alt={name} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      ) : (
        initials || "?"
      )}
    </span>
  );
}
