UI Scan Report - InaDigiWay
Date: 2026-02-09

Scope
- Full scan of HTML/CSS/JS files in the workspace (project templates, static assets, and collected static files).
- No changes applied. This report is informational only.

Entry Points and Templates
- Current live page: main/templates/main/home.html (extends base.html)
- Base layout and meta: main/templates/main/base.html
- Header/nav: main/templates/main/partials/_header.html
- Hero: main/templates/main/partials/_hero.html
- Services layout: main/templates/main/partials/_services_layout.html
- Services cards (legacy/alt): main/templates/main/partials/_services.html
- About: main/templates/main/partials/_about.html
- Happy clients: main/templates/main/partials/_happy_clients.html
- Contact: main/templates/main/partials/_contact.html
- Footer: main/templates/main/partials/_footer.html
- Legacy page: main/templates/index.html (appears unused by home.html)

Stylesheets and Scripts
- Active stylesheet: static/css/site.css
- Additional stylesheet (empty): static/css/style.css
- Collected static output: staticfiles/css/site.css (generated; do not edit directly)
- JS: static/js/site.js, static/js/sticky-mega-text.js, static/js/services-mobile-order.js
- Collected JS in staticfiles/ (generated; do not edit directly)

Key Findings (Layout/Style Conflicts)
1) Legacy vs. component layout overlap
   - Presence of legacy page main/templates/index.html suggests old image-based layout assumptions.
   - Current home.html uses component sections that rely on shared global rules in static/css/site.css.

2) Vertical/rotated text and sticky CTA in global styles
   - Vertical text and rotation appear in CSS for hero mega text and services mega text.
   - Sticky CTA uses vertical writing-mode and rotation.
   - These patterns are global and may leak into mobile when overrides are incomplete.

3) Multiple mobile overrides for the same sections
   - Several @media (max-width: 768px) blocks redefine layout behavior for header, hero, services, and mega text.
   - Duplication increases risk of conflicts and unpredictable behavior across breakpoints.

4) Width and margin constraints that force narrow content columns
   - Repeated use of 60% width with 20% margins in hero/services containers.
   - On mobile, these constraints can create unintended narrow columns and misalignment with background strips.

5) Sticky CTA and vertical mega text are not isolated
   - Styles target class names used in multiple sections, not scoped to a single page container.
   - This increases side effects on mobile layouts if any section changes.

6) Collected staticfiles/ directory contains a full copy of CSS/JS
   - Changes should only be made in static/ and templates/ to avoid being overwritten.

References (Examples)
- Vertical/rotated text rules: static/css/site.css
  - .hero__mega-text, .hero__mega-text-content
  - .services-layout__mega-text, .services-layout__mega-text-content
  - .sticky-cta__btn
- Mobile overrides: static/css/site.css
  - Multiple @media (max-width: 768px) blocks
- Legacy template: main/templates/index.html

Risks If Patching Continues Without Refactor
- New fixes may regress other sections due to shared rules.
- Mobile layout remains fragile because base styles are desktop-first with heavy overrides.
- Visual alignment will drift as more exceptions are added.

Recommended Next Steps (No Implementation Yet)
1) Confirm whether main/templates/index.html is truly unused and safe to treat as legacy.
2) Define a scoped wrapper for home.html (e.g., .home-page) and migrate section styles under it.
3) Create a mobile-first block for home sections only, with explicit component boundaries.
4) Consolidate duplicated mobile media rules into one per section.
5) Decide whether vertical mega text and sticky CTA should exist on mobile, then enforce with a single scoped rule.

Notes
- This report is based on file scan of HTML/CSS/JS and keyword searches for layout-affecting rules.
- No code changes made.
