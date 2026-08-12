import React, { createContext, useContext, useEffect, useState } from "react";

export type Theme = "light" | "dark";

interface ThemeContextValue {
  darkMode: boolean;
  setDarkMode: (next: boolean) => void;
}

const ThemeContext = createContext<ThemeContextValue | null>(null);

const STORAGE_KEY = "mkpicker:theme";

const DARK_QUERY = "(prefers-color-scheme: dark)";

/** Reads the saved theme, or null if the user has never picked one (or storage is unavailable). */
function readStoredTheme(): Theme | null {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    return stored === "dark" || stored === "light" ? stored : null;
  } catch {
    return null;
  }
}

/** The OS-level preference; light if the browser can't tell us. */
function readSystemTheme(): Theme {
  return window.matchMedia?.(DARK_QUERY).matches ? "dark" : "light";
}

/** Applies the active theme to <html data-theme> so tokens/colors.css can react to it. */
export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>(() => readStoredTheme() ?? readSystemTheme());

  useEffect(() => {
    if (theme === "dark") {
      document.documentElement.dataset.theme = "dark";
    } else {
      delete document.documentElement.dataset.theme;
    }
  }, [theme]);

  // Until the user picks a theme themselves, track the system preference live.
  useEffect(() => {
    if (readStoredTheme() !== null) return;
    const media = window.matchMedia?.(DARK_QUERY);
    if (!media) return;
    const onChange = (e: MediaQueryListEvent) => setTheme(e.matches ? "dark" : "light");
    media.addEventListener("change", onChange);
    return () => media.removeEventListener("change", onChange);
  }, [theme]);

  const value: ThemeContextValue = {
    darkMode: theme === "dark",
    setDarkMode: (next) => {
      const picked: Theme = next ? "dark" : "light";
      setTheme(picked);
      // Storage can throw in private-browsing modes — the theme still applies for this session.
      try {
        localStorage.setItem(STORAGE_KEY, picked);
      } catch {
        /* preference just won't persist */
      }
    },
  };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

// eslint-disable-next-line react-refresh/only-export-components -- hook is colocated with its provider
export function useTheme(): ThemeContextValue {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within a ThemeProvider");
  return ctx;
}
