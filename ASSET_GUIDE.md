# Asset Upload Guide

## 📁 Where to Add Your Files

### Project Images & Diagrams
**Location:** `src/assets/projects/`

Create this folder and add:
- `dns-migration.png` - DNS migration architecture diagram
- `network-automation.png` - Automation workflow diagram  
- `deep-space-network.png` - Network topology diagram

### Technology Icons
**Location:** `src/assets/tech-icons/`

Download SVG/PNG icons for:
- AWS, Azure, Python, Docker, Kubernetes
- Cisco, Palo Alto, Infoblox
- Linux, Git, Ansible

Recommended sources:
- https://devicon.dev/
- https://simpleicons.org/
- Official vendor sites

### Certification Badges
**Location:** `src/assets/certifications/`

Add your Credly badges:
1. Go to your Credly profile
2. Click on each badge
3. Select "Share" → "Download Badge"
4. Save as PNG with names like:
   - `ccna-badge.png`
   - `aws-cloud-architect.png`
   - `comptia-security-plus.png`
   - `comptia-network-plus.png`

## 🎨 Image Requirements

### Dimensions
- Project images: 1200x800px (landscape)
- Technology icons: 64x64px or SVG
- Certification badges: 200x200px
- Profile photo: 600x600px (square)

### Format & Optimization
- Use WebP for photos (better compression)
- Use SVG for logos/icons (scalable)
- Use PNG for badges with transparency
- Compress all images: https://tinypng.com/

## 📝 How to Add Credly Badges to HTML

After downloading your badges, add this section after Technologies:

```html
<!-- **** Certifications Section **** -->
<section id="certifications" style="padding: 5rem 0;">
  <div class="container">
    <h2 class="section-title">Certifications & Achievements</h2>
    <div style="display: flex; flex-wrap: wrap; gap: 2rem; justify-content: center; margin-top: 3rem;">
      
      <!-- CCNA Badge -->
      <div style="text-align: center;">
        <a href="YOUR_CREDLY_LINK" target="_blank">
          <img src="assets/certifications/ccna-badge.png" 
               alt="CCNA Certification" 
               style="width: 150px; height: 150px;">
        </a>
        <p style="margin-top: 0.5rem; font-weight: bold;">CCNA</p>
        <small>Enterprise Networking</small>
      </div>
      
      <!-- Add more badges similarly -->
      
    </div>
    
    <!-- Verification Link -->
    <div style="text-align: center; margin-top: 3rem;">
      <a href="https://www.credly.com/users/YOUR-USERNAME" 
         target="_blank" 
         class="cta-btn cta-btn--hero">
        View All Certifications on Credly
      </a>
    </div>
  </div>
</section>
```

## 🚀 Quick Setup Commands

```bash
# Create asset directories
mkdir -p src/assets/projects
mkdir -p src/assets/tech-icons
mkdir -p src/assets/certifications

# After adding images, optimize them
# Install image optimization tools
npm install --save-dev imagemin imagemin-webp

# Convert images to WebP (optional but recommended)
# Add to package.json scripts:
"optimize-images": "imagemin src/assets/**/*.{jpg,png} --out-dir=src/assets"
```

## 📊 Example Network Diagram

For your DNS Migration project, create a diagram showing:
- Source: BIND DNS servers
- Migration process (Python scripts)
- Target: Infoblox Grid
- Show "Zero Downtime" achievement

Tools for creating diagrams:
- draw.io (free, web-based)
- Lucidchart
- Microsoft Visio
- Python libraries (matplotlib, networkx)

## 🎯 Priority Assets to Add

1. **High Priority**
   - Your Credly certification badges
   - At least one network diagram
   - Updated profile photo (if needed)

2. **Medium Priority**
   - Technology icons for the skills section
   - Project screenshots or diagrams
   - NASA JPL logo (if permitted)

3. **Nice to Have**
   - Animation GIFs of automation in action
   - Dashboard screenshots
   - Before/after performance graphs

## 📌 Notes

- Always check image licensing before using
- Keep file sizes under 500KB for web performance
- Use descriptive alt text for accessibility
- Consider lazy loading for below-the-fold images
- Test on mobile devices for responsive display

---
*Remember: Good visuals make your portfolio memorable!*