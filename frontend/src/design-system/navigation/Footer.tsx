import React from "react";
import { Logo } from "../brand/Logo";
import { useTheme } from "../theme/ThemeContext";

export interface FooterLink {
  label: string;
  href: string;
}

export interface FooterProps extends React.HTMLAttributes<HTMLElement> {
  /** Placeholder links shown on the right. Defaults to a stub set. */
  links?: FooterLink[];
}

const defaultLinks: FooterLink[] = [
  { label: "About", href: "#" },
  { label: "Tracks", href: "#" },
  { label: "GitHub", href: "#" },
];

/**
 * MK Picker page footer — placeholder chrome that mirrors TopNav: logo lockup
 * on the left, stub links on the right, chunky ink border on top. Sits at the
 * bottom of the page; the Home column stretches the content above it so this
 * lands on the viewport floor even when a section is short.
 */
export function Footer({ links = defaultLinks, style, ...rest }: FooterProps) {
  const { darkMode } = useTheme();
  return (
    <footer
      style={{
        display: "flex",
        alignItems: "center",
        gap: 24,
        flexWrap: "wrap",
        padding: "20px 32px",
        marginTop: "auto",
        background: "var(--surface-cream)",
        borderTop: "var(--border-base) solid var(--border-ink)",
        fontFamily: "var(--font-body)",
        fontSize: "var(--text-sm)",
        color: "var(--text-muted)",
        ...style,
      }}
      {...rest}
    >
      <Logo variant="full" size={22} onDark={darkMode} />
      <span>Vote smarter. Placeholder footer — real content coming soon.</span>
      <nav style={{ display: "flex", gap: 20, marginLeft: "auto" }}>
        {links.map((link) => (
          <a
            key={link.label}
            href={link.href}
            style={{ color: "var(--text-link)", textDecoration: "none", fontWeight: "var(--weight-semibold)" }}
          >
            {link.label}
          </a>
        ))}
      </nav>
    </footer>
  );
}
