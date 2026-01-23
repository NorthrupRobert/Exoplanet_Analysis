[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NorthrupRobert/Exoplanet_Analysis/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fmain.ipynb)

# EXO-PLANET ANALYSIS
## *Analyzing means of exoplanet identification*

*Author:* Robb Northrup

*Date:* December 15, 2025 - CURRENT

*Links* 
 - [GitHub](https://www.github.com/NorthrupRobert/)
 - [LinkedIn](https://www.linkedin.com/in/robb-northrup-463867382)

## ABSTRACT


---

## KEY FINDINGS
(High level results)

---

## RECOMMENDED ACTIONS


---

## PROBLEM STATEMENT
### Analysis Problem
Exoplanet discoveries are heavily influenced by the limitaiton and biases imposed by our detection methods. As a result, certain star types appear to host far more planets due to the simplicity of viewing these star types, not necessarily because they actually have more planets. This project aims to nalyze detection bias across star types to help improve the accuracy of exoplanet occurrence estimates and guid future observational strategies.

### Overview
This project serves as an analysis of current methods being utilize to identify exoplanets within the visible universe in detection bias & star type:

**Question: Are we disproportionately finding planets around certain types of stars (e.g., red dwarfs) because of telescope sensitivity?**

**Importance: Highlights how our tools shape what we “see” and what we might be missing.**

### Success Metrics
1. *Cleaning:* % Usable Dataset Adjustment
2. *Bias:*

### Signifigance
Current exoplanet discoveries are affected heavily by our biases and limitations of our current means of detecting them. Particular types of stars, as a result of this, might appear to host planets much more than they actually do, seeing as these stars are easier to observe. The project here serves as an analysis of detection bias across star types to improve the accuracy of exoplanet occurance estimates and guide future observation expeditions.

---

## BACKGROUND
### What makes an Exoplanet?
Exoplanets are defined as planets outside of the Sol System (our solar system). Using our current methods of detection, 6061 exoplanets have been confirmed, based on a strict set of criteria:
According to the NASA Exoplanet Archive and other catalogs, the main criteria are:
- **Mass Limit:** Must be ≤ 30 Jupiter masses. Anything larger is considered a brown dwarf (a “failed star”)
- **Orbital Requirement:**
    - Must orbit a star (or stellar remnant).
    - Free-floating planets (rogue planets drifting through space) are excluded from most exoplanet catalogs
- **Validation:**
    - Must have sufficient follow-up observations (e.g., transit confirmation, radial velocity checks)
    - False positives (like binary stars mimicking planet signals) must be ruled out

### Classifying Stars
Stars are classified using the MK (Morgan-Keenan) system for spectral classification. This feature details the temperature and color of a star as a consequence of absorption features in the stellar spectra.

The first character of a star's classification (Harvard classification) is ultimately a consequence of the star's effective temperature (so far as main sequence stars are concerned), and are detailed as follows:
| CLASS | EFFECTIVE TEMPERATURE | CHOMATICITY | MAIN-SEQUENCE MASS (SOLAR MASSES) |
| ----- | --------------------- | ----------- | --------------------------------- |
| O | >=33000K | blue | >= 16M |
| B | 10000-33000K | deep blueish-white | 2.1-16M |
| A | 7300-10000K | blueish-white | 1.4-2.1M |
| F | 6000-7300K | white | 1.04-1.4M |
| G | 5300-6000K | yellowish-white | 0.8-1.04M |
| K | 3900-5300K | pale yellowish-orange | 0.45-0.8M |
| M | 2300-3900K | orangish-red | 0.08-0.45M |

The second character in this classification details the temperature of the star on a scale from 0-9 with respect to other stars within the same Harvard Classification.

Finally, the last character (or set of characters) identify the luminosity class of the star, which is based on the absorbtion lines of the given star... sharper more defined features in this spectra (typically of large, low-surface gravity stars) are high lumonocity bodies, whereas broader absorbtion lines are indicative of a lower lumonocity class. The lumonocity class is defined as follows:
| CLASS | PHYSICAL MEANING |
| I | Supergiants |
| II | Bright Giants |
| III | Giants |
| IV | Subgiants |
| V | Main Sequence (Dwarfs) |
| VI | Subdwarfs |
| VII | White Dwarfs |

A few example classifications are as follows:
- **G2V** A main sequence G-star that is closer in temperature to the F spectrum as opposed to the K (This is the Sun's classification!)
- **F5Ib** White, mid-temp F, less luminous supergiant
- **O1Ia** Deep-blue, incredibly hot O-star, luminous supergiant

### Distribution of Star Classifications
Following the Morgan-Keenan system, the distribution of stars are as follows:
- Main Sequence:
    - O 0.00003%
    - B 0.125%
    - A 0.625%
    - F 3.03%
    - G 7.5%
    - K 12%
    - M 76%
- Stars that do not fit this sequence:
    - W 
    - S
    - C
- Stellar Remenants
    - D
    - L
    - T
    - Y

### Detection Methods
- **Exoplanets**
    - Transit (a planet passes in front of a star)
    - Radial Velocity (a star's wobble)
    - Direct Imaging
    - Microlensing
- **Stars**

Each method has its own reliability thresholds before a candidate is confirmed.
Exoplanet

### Other Important Background Knowledge
 - **Paralax:** Measure of how close are far away a given star is. The Gaia dataset measures the incredibly tiny wobbles of stars in the sky (as Earth orbit around the sun), and measures the angles of the wobble. This is parallax, which is measured in milliarcseconds.
    - Large parallax -> close star
    - Small parallax -> far star

### Analysis
1. Compile data from the following datasets:
    - **Planetary System Composite Data** (NASA Exoplanet Archive) For analyzing detected exoplanets and their host stars
    - **Kepler Stellar** (NASA Exoplanet Archive) Exploring all stellar bodies targeted by the Kepler Space Telescope
    - **Gaia DR3** () Mass Dataset of all known stars in our observable universe.

---

## THE DATA
NASA's Exoplanet Archive (courtesy of CalTech and NASA) "Planetary Systems" dataset was utilized to examen the features in question. Information was compiled by utilzing the TAP (Table Access Protocol) API, the prime standard as defined by the IVOA (International Virtual Observatory Alliance). TAP is standardized as to not be limited to NASA datasets, but instead utilized cross-organizationally

---

## METHODOLOGY
### High Level Workflow
### Harvard Star Classification based on Star Effective Temperature for Handling Unknown Spectral Types
Wikipedia (https://en.wikipedia.org/wiki/Stellar_classification): "Harvard astronomer Cecilia Payne then demonstrated that the O-B-A-F-G-K-M spectral sequence is actually a sequence in temperature.[19] Because the classification sequence predates our understanding that it is a temperature sequence, the placement of a spectrum into a given subtype, such as B3 or A7, depends upon (largely subjective) estimates of the strengths of absorption features in stellar spectra. As a result, these subtypes are not evenly divided into any sort of mathematically representable intervals."

---

## DATA EXPLORATION


---

## DETAILED RESULTS


---

## FUTURE WORK


---

## Room for Improvement

### Questions that I would like to Address in the Future

1. The Goldilocks Dilemna
	Europa (one of the Galilean moons of Jupiter) is a clear example of a breeding ground for life beyond Earth that challenges the notion of the goldilocks zone being the only habitable area from which habitable exoplanets can be reasonably identified. This moon challenges that notion, and could alter how we choose to identify habitable exoplanets and exomoons forever. If we adjusted habitable exoplanet analysis for undersurface seas for interstellar object outside the goldilocks zone?

	Why it stands out: Challenges our currents means for identifying exoplanets, potentially opening up the door for thousands of more identifyable exoplanets from the data we already have collected.

2. Exoplanet Blindspot
	How many exoplanets could we reasonably expect to find should we eliminate our geometric oversights (such as transit identification being dependent on the planet falling within our line of sight) for all star types, not just proxi-suns?

---

## SOURCES