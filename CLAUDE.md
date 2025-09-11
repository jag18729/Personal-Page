# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Build and Development
- **Start development server**: `npm start` - Runs Parcel dev server at http://localhost:1234
- **Production build**: `npm run build` - Builds production files to `dist/` folder
- **Install dependencies**: `npm install`

### Code Formatting
- **Format code**: `npx prettier --write .` - Formats files using Prettier configuration

## Project Architecture

This is a personal portfolio website for Rafael Garcia, a Network Development Engineer at NASA JPL. The project uses a modern static site architecture:

### Tech Stack
- **Build Tool**: Parcel 2.x - Zero-configuration build tool
- **Styling**: SCSS/Sass with Bootstrap 5
- **JavaScript**: Vanilla JS with ScrollReveal and Tilt animations
- **Dependencies**: jQuery, Bootstrap, Material-UI components

### Directory Structure
```
src/
├── index.html          # Main HTML file (entry point)
├── styles.scss         # Main stylesheet entry
├── index.js           # Main JavaScript entry
├── assets/            # Images, resume PDF, favicon
├── sass/              # SCSS organized by architecture
│   ├── abstracts/     # Variables, mixins, helpers
│   ├── base/          # Base styles, typography
│   ├── components/    # Buttons, reusable components
│   ├── layout/        # Footer, sections layout
│   ├── sections/      # About, contact, hero, projects
│   └── vendors/       # Bootstrap imports
├── scripts/           # JavaScript modules
└── data/              # Configuration files
```

### Key Features
- **Sections**: Hero, About, Technologies, Certifications, Projects, Contact
- **Animations**: ScrollReveal for section reveals, Vanilla Tilt for project cards
- **Responsive**: Bootstrap-based responsive design
- **PDF Resume**: Embedded resume viewing capability

### Deployment
- **CI/CD**: GitHub Actions workflow deploys to GitHub Pages on main branch pushes
- **Build Output**: Files are built to `dist/` directory
- **Live URL**: https://jag18729.github.io/Personal-Page/

### Content Management
The portfolio content is primarily in `src/index.html` with styling in the SCSS files. Personal information, projects, and technologies are directly embedded in the HTML structure.

### Security Tools
The repository includes Python security scanning scripts in `src/scripts/` for port scanning and vulnerability checking - these are for educational/defensive purposes only.