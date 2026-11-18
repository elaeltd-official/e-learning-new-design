# E-Learning Platform Redesign (E-Lae Ltd)

A modern, high-converting E-Learning platform landing page for E-Lae Ltd, featuring an interactive district campus locator, live career track funnel, dynamic syllabus detail drawers, verified trainer directory, student success stories, and press coverage.

## Project Architecture & Modular Sections

To ensure maintainability and eliminate the need to read huge monolithic files repeatedly, the project is structured into clean modular sections under `sections/`:

```text
├── sections/                       # Modular section HTML files
│   ├── 00-head.html                # Metadata, fonts, and Tailwind styles
│   ├── 01-top-banner.html          # Top announcement & hotline bar
│   ├── 02-navbar.html              # Sticky navigation & mega-menu
│   ├── 03-hero.html                # Hero section & impact metrics
│   ├── 04-course-categories.html   # Course categories & career tracks
│   ├── 05-course-catalog.html      # 16-course catalog with EMI & syllabus preview
│   ├── 06-campus-locator.html      # 64-district interactive campus locator
│   ├── 07-government-initiatives.html # National AI & youth skills initiatives
│   ├── 08-career-funnel.html       # 3-step interactive career course funnel
│   ├── 09-mentors-faculty.html     # Mentors & faculty directory modal
│   ├── 10-success-stories.html     # Video gallery & student documentary cards
│   ├── 11-news-feeds.html          # Press & national media coverage
│   ├── 12-free-seminars.html       # Free live masterclass & counseling
│   ├── 13-blog-insights.html       # Thought leadership & career insights
│   ├── 14-faq.html                 # Structured schema FAQ accordion
│   ├── 15-footer.html              # Enterprise footer & copyright
│   ├── 16-floating-bar.html        # Quick enrollment bottom bar
│   ├── 17-modals.html              # Dynamic syllabus, video & directory modals
│   └── 18-scripts.html             # Client-side JavaScript interactions
├── assets/                         # Static assets (images, news, maps)
│   ├── logo.webp
│   ├── maps/
│   └── news/
├── index.html                      # Compiled, production-ready landing page
├── trainer-profile.html            # Dedicated trainer authority profile page
├── build.py                        # Ultra-fast (~0.05s) section compiler
└── README.md
```

## How to Build

Run the compiler script anytime a section in `sections/` is updated:

```bash
python build.py
```

It compiles all 19 section files in order into `index.html` and `index_elaeltd_redesign.html` in under 0.1 seconds with 100% byte-for-byte fidelity.
