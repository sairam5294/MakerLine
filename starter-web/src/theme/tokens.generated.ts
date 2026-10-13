// ⚠️ GENERATED from design/tokens.json by design/build-tokens.mjs — do not edit by hand.
// Change tokens.json (or sync it from Figma), then run: npm run tokens

export const palette = {
  "white": "#FFFFFF",
  "black": "#000000",
  "gray50": "#F7F7F8",
  "gray100": "#EDEDEF",
  "gray300": "#C4C4CC",
  "gray600": "#5C5C66",
  "gray800": "#2A2A31",
  "gray900": "#16161A",
  "blue300": "#A6C4FF",
  "blue400": "#7AA7FF",
  "blue600": "#1F5FD1",
  "blue700": "#174CAB",
  "red400": "#FF8A80",
  "red700": "#B42318",
  "green400": "#6FD39A",
  "green700": "#1E7A46"
} as const;

export type SemanticColor = 'background' | 'surface' | 'border' | 'textPrimary' | 'textSecondary' | 'textOnPrimary' | 'primary' | 'primaryPressed' | 'danger' | 'success' | 'focusRing';
export type ColorTokens = Record<SemanticColor, string>;

export const lightColors: ColorTokens = {
  "background": "#FFFFFF",
  "surface": "#F7F7F8",
  "border": "#5C5C66",
  "textPrimary": "#16161A",
  "textSecondary": "#5C5C66",
  "textOnPrimary": "#FFFFFF",
  "primary": "#1F5FD1",
  "primaryPressed": "#174CAB",
  "danger": "#B42318",
  "success": "#1E7A46",
  "focusRing": "#1F5FD1"
};

export const darkColors: ColorTokens = {
  "background": "#16161A",
  "surface": "#2A2A31",
  "border": "#C4C4CC",
  "textPrimary": "#F7F7F8",
  "textSecondary": "#C4C4CC",
  "textOnPrimary": "#16161A",
  "primary": "#7AA7FF",
  "primaryPressed": "#A6C4FF",
  "danger": "#FF8A80",
  "success": "#6FD39A",
  "focusRing": "#7AA7FF"
};

export const space = {
  "xs": 4,
  "sm": 8,
  "md": 16,
  "lg": 24,
  "xl": 32,
  "xxl": 48
} as const;

export const radius = {
  "sm": 6,
  "md": 10,
  "lg": 16,
  "pill": 999
} as const;

export const type = {
  "title": {
    "fontSize": 28,
    "lineHeight": 34,
    "fontWeight": "700"
  },
  "heading": {
    "fontSize": 20,
    "lineHeight": 26,
    "fontWeight": "600"
  },
  "body": {
    "fontSize": 16,
    "lineHeight": 24,
    "fontWeight": "400"
  },
  "label": {
    "fontSize": 14,
    "lineHeight": 20,
    "fontWeight": "600"
  },
  "caption": {
    "fontSize": 13,
    "lineHeight": 18,
    "fontWeight": "400"
  }
} as const;

export const minTouchTarget = 48;

export const motion = {
  "fast": 150,
  "normal": 250
} as const;

/** Colour pairs that must pass WCAG 2.2 AA (4.5 = text, 3 = large text / UI boundaries). */
export const contrastPairs: { fg: SemanticColor; bg: SemanticColor; min: number }[] = [
  {
    "fg": "textPrimary",
    "bg": "background",
    "min": 4.5
  },
  {
    "fg": "textPrimary",
    "bg": "surface",
    "min": 4.5
  },
  {
    "fg": "textSecondary",
    "bg": "background",
    "min": 4.5
  },
  {
    "fg": "textSecondary",
    "bg": "surface",
    "min": 4.5
  },
  {
    "fg": "textOnPrimary",
    "bg": "primary",
    "min": 4.5
  },
  {
    "fg": "textOnPrimary",
    "bg": "primaryPressed",
    "min": 4.5
  },
  {
    "fg": "primary",
    "bg": "background",
    "min": 4.5
  },
  {
    "fg": "danger",
    "bg": "background",
    "min": 4.5
  },
  {
    "fg": "success",
    "bg": "background",
    "min": 4.5
  },
  {
    "fg": "border",
    "bg": "background",
    "min": 3
  },
  {
    "fg": "focusRing",
    "bg": "background",
    "min": 3
  }
];
