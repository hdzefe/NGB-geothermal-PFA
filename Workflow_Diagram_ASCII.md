```
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                        NORTH GERMAN BASIN: 18-HORIZON RESERVOIR FAVORABILITY ANALYSIS                                            ║
║                              Independent PFA with Composite Stacking Analysis                                                     ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝


┌─────────────────────────────────┐     ┌────────────────────────────────────────┐     ┌─────────────────────────────────┐
│      INPUT LAYERS               │     │   WEIGHTED SUMMATION PROCESS          │     │   FAVORABILITY MAP              │
│                                 │     │                                        │     │                                 │
│  GEOLOGICAL CRITERIA            │     │                                        │     │  HORIZON 1:                     │
│  (Per Horizon)                  │     │  Weight:                               │     │  Vatangin-Bueckeberg           │
│                                 │     │  0.30 (Thermal)                       │     │                                 │
│ • Synthetic Thermal             │─────┼──► Summation (⊗) ─────┐              │     │  [0-5 Favorability Map]        │
│   Horizon #1 [°C at depth]      │     │                      │               │     │                                 │
│                                 │     │                      ▼               │     │  ┌───────────────────────────┐  │
│ • TUNB Depth Surface            │     │         Geological Summary Layer      │     │  │ Red: Favorability 4-5     │  │
│   [m below surface]             │     │                                       │     │  │ Yel: Favorability 2.5-4   │  │
│                                 │     │  Weight:                              │     │  │ Blu: Favorability 0-2.5   │  │
│ • Heat Flow                     │─────┼──► 0.70 (Geologic)                  │     │  └───────────────────────────┘  │
│   [mW/m²]                       │     │                                       │     │                                 │
│                                 │     │                      ┌────────────────┤     │                                 │
│ • Prospective Sandstones        │     │                      │                │     │                                 │
│   (Vatangin-Bueckeberg type)    │─────┼──► Summation (⊗) ──┤                │     │                                 │
│   [probability/thickness]       │     │                      │                │     │                                 │
│                                 │     │  Weight:             │                │     │                                 │
│ • Salt Structures (Distance)    │     │  0.5 (Combined)      │                │     │                                 │
│   [km from seal]                │─────┼──►                   │                │     │                                 │
│                                 │     │                      ▼                │     │                                 │
│ • Geothermal Evidence           │     │         GEOLOGICAL SUMMARY LAYER      │     │                                 │
│   (Boreholes - Vatangin unit)   │─────┼──►                                    │     │                                 │
│   [km distance]                 │     │                                        │     │                                 │
│                                 │     │                                        │     │                                 │
└─────────────────────────────────┘     │                                        │     │                                 │
         ↓ ↓ ↓                           │                                        │     │                                 │
         [FOR EACH OF 18 HORIZONS]       │                                        │     │                                 │
┌─────────────────────────────────┐     │                                        │     │                                 │
│      INPUT LAYERS               │     │                                        │     │                                 │
│                                 │     │                                        │     │  HORIZON 2:                     │
│  GEOLOGICAL CRITERIA            │     │  Weight:                               │     │  Middle-Bunter Sand            │
│  (Per Horizon)                  │     │  0.30 (Thermal)                       │     │                                 │
│                                 │     │                                        │     │  [0-5 Favorability Map]        │
│ • Synthetic Thermal             │─────┼──► Summation (⊗) ─────┐              │     │                                 │
│   Horizon #2 [°C at depth]      │     │                      │               │     │  ┌───────────────────────────┐  │
│                                 │     │                      ▼               │     │  │ Red: Favorability 4-5     │  │
│ • TUNB Depth Surface            │     │         Geological Summary Layer      │     │  │ Yel: Favorability 2.5-4   │  │
│   [m below surface]             │     │                                       │     │  │ Blu: Favorability 0-2.5   │  │
│                                 │     │  Weight:                              │     │  └───────────────────────────┘  │
│ • Heat Flow                     │─────┼──► 0.70 (Geologic)                  │     │                                 │
│   [mW/m²]                       │     │                                       │     │                                 │
│                                 │     │                      ┌────────────────┤     │                                 │
│ • Prospective Sandstones        │     │                      │                │     │                                 │
│   (Middle-Bunter type)          │─────┼──► Summation (⊗) ──┤                │     │                                 │
│   [probability/thickness]       │     │                      │                │     │                                 │
│                                 │     │  Weight:             │                │     │                                 │
│ • Salt Structures (Distance)    │     │  0.5 (Combined)      │                │     │                                 │
│   [km from seal]                │─────┼──►                   │                │     │ ... (Horizons 3-17)            │
│                                 │     │                      ▼                │     │                                 │
│ • Geothermal Evidence           │     │         GEOLOGICAL SUMMARY LAYER      │     │                                 │
│   (Boreholes - Middle-Bunter)   │─────┼──►                                    │     │                                 │
│   [km distance]                 │     │                                        │     │  HORIZON 18:                    │
│                                 │     │                                        │     │  [Deepest/Latest Horizon]      │
└─────────────────────────────────┘     │                                        │     │                                 │
         ↓ ↓ ↓                           │                                        │     │  [0-5 Favorability Map]        │
         [×18 HORIZONS]                  │                                        │     │                                 │
                                         │                                        │     │  ┌───────────────────────────┐  │
┌─────────────────────────────────┐     │                                        │     │  │ Red: Favorability 4-5     │  │
│      INPUT LAYERS               │     │  Weight:                               │     │  │ Yel: Favorability 2.5-4   │  │
│                                 │     │  0.30 (Thermal)                       │     │  │ Blu: Favorability 0-2.5   │  │
│  ECONOMIC CRITERIA              │     │                                        │     │  └───────────────────────────┘  │
│  (SHARED ACROSS ALL HORIZONS)   │     │  ┌──────────────────────────────┐     │     │                                 │
│                                 │     │  │                              │     │     └─────────────────────────────────┘
│ • Population Density            │─────┼──┼─► Summation (⊗)             │     │
│   [people/km²]                  │     │  │       Weight: 0.273         │     │
│                                 │     │  │                              │     │
│ • District Heating Network      │─────┼──┼─►                           │     │
│   Distance [km]                 │     │  │                              │     │
│                                 │     │  │   ECONOMIC SUMMARY LAYER     │     │
│ • Upstream Petroleum            │─────┼──┼─►                           │     │
│   Electrification              │     │  │   Weight: 0.5                │     │
│   [feasibility index]           │     │  │   (APPLIED TO ALL HORIZONS) │     │
│                                 │     │  │                              │     │
│ • Electrical Infrastructure     │─────┼──┼─► Summation (⊗)             │     │
│   [km distance to grid]         │     │  │       Weight: 0.273         │     │
│                                 │     │  │                              │     │
│ • Proposed Electrical           │─────┼──┼─►                           │     │
│   Infrastructure                │     │  │                              │     │
│   [km distance]                 │     │  │                              │     │
│                                 │     │  │                              │     │
└─────────────────────────────────┘     │  └──────────────────────────────┘     │
                                         │                                        │
                                         │                                        │
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                          POST-PROCESSING: COMPOSITE STACKING ANALYSIS                                             ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                                                    ║
║  STEP 1: Stack all 18 favorability maps geographically                                                                           ║
║  STEP 2: Count # of favorable horizons per location (threshold: favorability > 3.0)                                              ║
║  STEP 3: Classify locations by stacking richness                                                                                ║
║                                                                                                                                    ║
║                    ┌────────────────────────────────────────────────┐                                                             ║
║                    │   COMPOSITE STACKING MAP                       │                                                             ║
║                    │   (Output)                                     │                                                             ║
║                    │                                                 │                                                             ║
║                    │  Red Zones: 4-6 horizons favorable             │                                                             ║
║                    │  → PRIMARY TARGETS (multi-pool play)           │                                                             ║
║                    │  → Multiple fallback reservoirs available      │                                                             ║
║                    │                                                 │                                                             ║
║                    │  Orange Zones: 2-3 horizons favorable          │                                                             ║
║                    │  → SECONDARY TARGETS                           │                                                             ║
║                    │  → Some fallback options available             │                                                             ║
║                    │                                                 │                                                             ║
║                    │  Yellow Zones: 1 horizon favorable             │                                                             ║
║                    │  → EXPLORATION ONLY (High Risk)                │                                                             ║
║                    │  → NO fallback if primary horizon is dry       │                                                             ║
║                    │                                                 │                                                             ║
║                    │  Blue Zones: 0 horizons favorable              │                                                             ║
║                    │  → AVOID                                       │                                                             ║
║                    │  → No viable geothermal resource                │                                                             ║
║                    │                                                 │                                                             ║
║                    └────────────────────────────────────────────────┘                                                             ║
║                                                                                                                                    ║
║  EXPLORATION STRATEGY:                                                                                                           ║
║  ✓ Drill in Red zones first → Primary target (e.g., Horizon 2 or 5)                                                              ║
║  ✓ If primary horizon is dry → Fallback to secondary horizon in same location                                                   ║
║  ✓ Example: Location A has Horizons 2, 5, 6 favorable                                                                             ║
║             Drill H2 first, fallback to H5, then H6 if needed                                                                     ║
║                                                                                                                                    ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝


KEY METHODOLOGICAL FEATURES:
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

1. INDEPENDENT HORIZONS (NOT Aggregated):
   • Each horizon (1-18) processed separately with unique thermal & geologic data
   • No black-box aggregation → Each result is transparent and reproducible
   • Can validate/update individual horizons without affecting others

2. HORIZON-SPECIFIC INPUTS:
   • Thermal data: Different synthetic thermal grid per horizon (different depths/temperatures)
   • Geologic data: Different sandstone types, seal configurations, boreholes per horizon
   • Economic data: SHARED across all horizons (demand, infrastructure, access)

3. WEIGHTED SUMMATION:
   • Layer level: Voter equation combines evidence within each component
   • Component level: Modified veto combines thermal + geologic per horizon
   • Criterion level: Economic gate-keeper applied across all horizons

4. COMPOSITE STACKING (Post-Processing):
   • NOT an aggregation during modeling
   • Simple overlay & counting of favorable horizons
   • Identifies locations with multiple stacked reservoirs (multi-pool plays)
   • Shows primary targets vs. fallback options

5. EXPLORATION RELEVANCE:
   • Each drilling location targets ONE horizon at a time
   • Stacking map shows where fallback reservoirs are available
   • Risk assessment transparent: single-horizon (risky) vs. multi-horizon (safer)

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

WEIGHTS SUMMARY:
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

ECONOMIC CRITERIA (shared across all 18 horizons):      Weight = 0.30
  ├─ Population Density                                Weight = 0.273
  ├─ District Heating Network Distance                Weight = 0.273
  ├─ Upstream Petroleum Electrification               Weight = 0.273
  ├─ Electrical Infrastructure Distance               Weight = 0.181
  └─ Proposed Electrical Infrastructure Distance      Weight = 0

PER HORIZON (Example: Vatangin-Bueckeberg):            Weight = 0.035
  ├─ THERMAL COMPONENT                               Weight = 0.60 (Pr0 = 0.60)
  │  ├─ Synthetic Thermal Horizon #1 [°C]            Weight = 0.30
  │  ├─ TUNB Depth Surface [m bsl]                   Weight = 0.40
  │  └─ Heat Flow [mW/m²]                            Weight = 0.30
  │
  └─ GEOLOGIC COMPONENT                              Weight = 0.40 (Pr0 = 0.50)
     ├─ Prospective Sandstones [prob]                Weight = 0.50
     ├─ Salt Structures Distance [km]                Weight = 0.30
     └─ Geothermal Evidence (Boreholes) [km]         Weight = 0.20

[Repeat for Horizons 2-18 with horizon-specific data]

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
```

---

## **WORKFLOW TEXT DESCRIPTION (for paper caption)**

> **Figure X: North German Basin 18-Horizon Independent Favorability Analysis Workflow**

> **(Left) Input Layers:** Raw exploration data organized into Geological Criteria (horizon-specific: synthetic thermal horizons, TUNB depth surfaces, heat flow, prospective sandstones, salt structures, geothermal evidence) and Economic Criteria (shared across all 18 horizons: population density, district heating network, electrical infrastructure).

> **(Middle) Weighted Summation Process:** Each horizon undergoes independent weighting: Geological components (Thermal: 60%, Geologic: 40%) are combined using voter equation with prior probabilities (Pr0); Economic component (30% weight) applied as gate-keeper across all horizons. Horizon-specific weights reflect unique geologic characteristics.

> **(Right) Favorability Maps:** 18 independent maps produced (one per horizon: Vatangin-Bueckeberg, Middle-Bunter Sand, Horizons 3-18), each showing favorability scores 0-5 (red=high, yellow=moderate, blue=low).

> **Post-Processing: Composite Stacking Analysis** (bottom) stacks all 18 favorability maps geographically to identify locations with multiple favorable horizons. Red zones indicate 4-6 favorable horizons (primary targets with multiple fallback reservoirs); orange zones 2-3 favorable (secondary targets); yellow zones 1 favorable (risky, no fallback); blue zones 0 favorable (avoid). This transparent, reservoir-specific approach enables robust exploration strategy with fallback options.
