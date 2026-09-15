"""
Generate workflow diagram for North German Basin PFA
CORRECTED VERSION: Matches actual data structure from table
- 2 Main Criteria: ECONOMIC + GEOTHERMAL
- Economic: 2 Components (Demand, Infrastructure)
- Geothermal: 3 Components (Thermal, Geologic, Geothermal Evidence)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

def generate_workflow_diagram_corrected():
    """
    Generate professional workflow diagram matching actual data structure
    Output: PNG (300 DPI for publication)
    """
    
    fig, ax = plt.subplots(figsize=(24, 16), dpi=100)
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Define colors
    color_economic_input = '#E1BEE7'  # Light purple
    color_geothermal_input = '#B3E5FC'  # Light cyan/blue
    color_demand_comp = '#FFE0B2'  # Light orange
    color_infra_comp = '#FFCCBC'  # Light coral
    color_thermal_comp = '#C8E6C9'  # Light green
    color_geologic_comp = '#FFF9C4'  # Light yellow
    color_evidence_comp = '#D1C4E9'  # Light indigo
    color_output = '#FFCCBC'  # Peach
    
    # ========== TITLE ==========
    ax.text(12, 15.5, 'NORTH GERMAN BASIN: 18-HORIZON RESERVOIR FAVORABILITY ANALYSIS', 
            fontsize=16, fontweight='bold', ha='center')
    ax.text(12, 15.0, 'Workflow: Input Layers → Weighted Components → Independent Horizon Maps → Composite Stacking', 
            fontsize=11, ha='center', style='italic', color='gray')
    
    # ========== LEFT COLUMN: INPUT LAYERS ==========
    y_start = 14
    
    ax.text(1.5, y_start, 'INPUT LAYERS', fontsize=13, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgray', edgecolor='black', linewidth=2))
    
    # ECONOMIC CRITERIA INPUTS
    ax.text(1.5, y_start-0.6, 'ECONOMIC CRITERIA', fontsize=11, fontweight='bold', 
            ha='center', color='#6A1B9A')
    
    econ_inputs = [
        ('Admin areas &\npopulation', y_start-1.3),
        ('GeoIS Heat\nDemand', y_start-2.0),
        ('District Heating\nNetwork', y_start-2.7),
        ('Waste Heat\nplatform (PfA)', y_start-3.4),
        ('Solar thermal\npotential', y_start-4.1),
    ]
    
    for label, y_pos in econ_inputs:
        box = FancyBboxPatch((0.4, y_pos-0.3), 2.2, 0.55, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#6A1B9A', facecolor=color_economic_input, linewidth=1.5)
        ax.add_patch(box)
        ax.text(1.5, y_pos, label, fontsize=8.5, ha='center', va='center', fontweight='bold')
    
    # Separator
    ax.plot([0.2, 2.8], [y_start-4.5, y_start-4.5], 'k-', linewidth=2)
    
    # GEOTHERMAL CRITERIA INPUTS
    ax.text(1.5, y_start-5.2, 'GEOTHERMAL CRITERIA', fontsize=11, fontweight='bold', 
            ha='center', color='#0277BD')
    
    geo_inputs = [
        ('GeoIS subsurface\ntemperatures', y_start-5.9),
        ('TUNB depth\nsurfaces', y_start-6.6),
        ('Heat Flow', y_start-7.3),
        ('Subsurface reservoir\nmaps "Sandsteinfazies"', y_start-8.0),
        ('Subsurface reservoir\nmaps "GeoPoNND"', y_start-8.7),
        ('Prospective Sandstones\n(Valangin-Bueckeberg)', y_start-9.4),
        ('Middle Bunter Sand\nquality', y_start-10.1),
        ('Salt structures', y_start-10.8),
        ('Deep hydrothermal\nsites', y_start-11.5),
        ('Puroperm\nborehole', y_start-12.2),
    ]
    
    for label, y_pos in geo_inputs:
        box = FancyBboxPatch((0.4, y_pos-0.3), 2.2, 0.55, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#0277BD', facecolor=color_geothermal_input, linewidth=1.5)
        ax.add_patch(box)
        ax.text(1.5, y_pos, label, fontsize=8, ha='center', va='center', fontweight='bold')
    
    ax.text(1.5, y_start-12.9, 'FOR EACH OF 18 HORIZONS', fontsize=10, fontweight='bold', 
            ha='center', color='red', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    # ========== MIDDLE COLUMN: COMPONENTS & WEIGHTING ==========
    
    ax.text(12, y_start, 'WEIGHTED COMPONENT PROCESS', fontsize=13, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgray', edgecolor='black', linewidth=2))
    
    # ECONOMIC CRITERIA PROCESSING
    ax.text(6.5, y_start-0.6, 'ECONOMIC CRITERIA', fontsize=11, fontweight='bold', 
            ha='left', color='#6A1B9A')
    
    # Demand Component
    demand_y = y_start - 1.5
    box = FancyBboxPatch((5.5, demand_y-0.4), 3.5, 0.8, 
                        boxstyle="round,pad=0.08", 
                        edgecolor='#E65100', facecolor=color_demand_comp, linewidth=2)
    ax.add_patch(box)
    ax.text(7.25, demand_y, 'DEMAND COMPONENT\nWeight: 0.50', fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Arrows from economic inputs to demand
    for label, y_pos in econ_inputs[:3]:
        arrow = FancyArrowPatch((2.6, y_pos), (5.5, demand_y),
                               arrowstyle='->', mutation_scale=15, linewidth=1.2, 
                               color='#6A1B9A', alpha=0.5)
        ax.add_patch(arrow)
    
    # Infrastructure Component
    infra_y = y_start - 3.5
    box = FancyBboxPatch((5.5, infra_y-0.4), 3.5, 0.8, 
                        boxstyle="round,pad=0.08", 
                        edgecolor='#D84315', facecolor=color_infra_comp, linewidth=2)
    ax.add_patch(box)
    ax.text(7.25, infra_y, 'INFRASTRUCTURE COMPONENT\nWeight: 0.50', fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Arrows from economic inputs to infrastructure
    for label, y_pos in econ_inputs[2:]:
        arrow = FancyArrowPatch((2.6, y_pos), (5.5, infra_y),
                               arrowstyle='->', mutation_scale=15, linewidth=1.2, 
                               color='#6A1B9A', alpha=0.5)
        ax.add_patch(arrow)
    
    # Separator
    ax.plot([5, 9.5], [y_start-4.5, y_start-4.5], 'k-', linewidth=2)
    
    # GEOTHERMAL CRITERIA PROCESSING
    ax.text(6.5, y_start-5.2, 'GEOTHERMAL CRITERIA', fontsize=11, fontweight='bold', 
            ha='left', color='#0277BD')
    
    # Thermal Component
    thermal_y = y_start - 6.2
    box = FancyBboxPatch((5.5, thermal_y-0.4), 3.5, 0.8, 
                        boxstyle="round,pad=0.08", 
                        edgecolor='#1B5E20', facecolor=color_thermal_comp, linewidth=2)
    ax.add_patch(box)
    ax.text(7.25, thermal_y, 'THERMAL COMPONENT\nWeight: 0.60 | Pr0: 0.60', fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Arrows from geothermal inputs to thermal
    for label, y_pos in geo_inputs[:3]:
        arrow = FancyArrowPatch((2.6, y_pos), (5.5, thermal_y),
                               arrowstyle='->', mutation_scale=15, linewidth=1.2, 
                               color='#0277BD', alpha=0.5)
        ax.add_patch(arrow)
    
    # Geologic Component
    geologic_y = y_start - 8.2
    box = FancyBboxPatch((5.5, geologic_y-0.4), 3.5, 0.8, 
                        boxstyle="round,pad=0.08", 
                        edgecolor='#F57F17', facecolor=color_geologic_comp, linewidth=2)
    ax.add_patch(box)
    ax.text(7.25, geologic_y, 'GEOLOGIC COMPONENT\nWeight: 0.35 | Pr0: 0.50', fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Arrows from geothermal inputs to geologic
    for label, y_pos in geo_inputs[3:8]:
        arrow = FancyArrowPatch((2.6, y_pos), (5.5, geologic_y),
                               arrowstyle='->', mutation_scale=15, linewidth=1.2, 
                               color='#0277BD', alpha=0.5)
        ax.add_patch(arrow)
    
    # Geothermal Evidence Component
    evidence_y = y_start - 10.2
    box = FancyBboxPatch((5.5, evidence_y-0.4), 3.5, 0.8, 
                        boxstyle="round,pad=0.08", 
                        edgecolor='#4527A0', facecolor=color_evidence_comp, linewidth=2)
    ax.add_patch(box)
    ax.text(7.25, evidence_y, 'GEOTHERMAL EVIDENCE\nWeight: 0.05 | Pr0: 0.30', fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Arrows from geothermal inputs to evidence
    for label, y_pos in geo_inputs[8:]:
        arrow = FancyArrowPatch((2.6, y_pos), (5.5, evidence_y),
                               arrowstyle='->', mutation_scale=15, linewidth=1.2, 
                               color='#0277BD', alpha=0.5)
        ax.add_patch(arrow)
    
    # Voter-Veto Equations
    ax.text(6.5, y_start-11.5, 'Voter Equation (per component):', fontsize=8, ha='left', style='italic', fontweight='bold')
    ax.text(6.5, y_start-11.9, 'P(Component|Evidence) = 1 / (1 + exp(-(w₀ + Σ wᵢ·zᵢ)))', 
            fontsize=7, ha='left', style='italic', family='monospace')
    ax.text(6.5, y_start-12.3, 'where w₀ = log(Pr0/(1-Pr0))', 
            fontsize=7, ha='left', style='italic', family='monospace')
    
    # ========== RIGHT COLUMN: OUTPUT FAVORABILITY MAPS ==========
    
    ax.text(19.5, y_start, 'FAVORABILITY MAPS', fontsize=13, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgray', edgecolor='black', linewidth=2))
    
    ax.text(19.5, y_start-0.7, 'INDEPENDENT HORIZON MAPS', fontsize=11, fontweight='bold', 
            ha='center', color='#D32F2F')
    
    # Arrows from components to output
    arrow = FancyArrowPatch((9.0, demand_y), (17.5, y_start-2.0),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#E65100', alpha=0.6)
    ax.add_patch(arrow)
    
    arrow = FancyArrowPatch((9.0, infra_y), (17.5, y_start-2.0),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#D84315', alpha=0.6)
    ax.add_patch(arrow)
    
    arrow = FancyArrowPatch((9.0, thermal_y), (17.5, y_start-2.0),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#1B5E20', alpha=0.6)
    ax.add_patch(arrow)
    
    arrow = FancyArrowPatch((9.0, geologic_y), (17.5, y_start-2.0),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#F57F17', alpha=0.6)
    ax.add_patch(arrow)
    
    arrow = FancyArrowPatch((9.0, evidence_y), (17.5, y_start-2.0),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#4527A0', alpha=0.6)
    ax.add_patch(arrow)
    
    # Horizon output maps
    horizon_outputs = [
        ('HORIZON 1:\nVatangin-Bueckeberg\n\nFavorability: 0-5', y_start-2.0),
        ('HORIZON 2:\nMiddle-Bunter Sand\n\nFavorability: 0-5', y_start-4.0),
        ('HORIZONS 3-17:\n...\n\nFavorability: 0-5', y_start-6.0),
        ('HORIZON 18:\n[Deepest Horizon]\n\nFavorability: 0-5', y_start-8.0),
    ]
    
    for label, y_pos in horizon_outputs:
        box = FancyBboxPatch((17.5, y_pos-0.6), 5.0, 1.2, 
                            boxstyle="round,pad=0.08", 
                            edgecolor='#D32F2F', facecolor=color_output, linewidth=2)
        ax.add_patch(box)
        ax.text(20, y_pos, label, fontsize=9, ha='center', va='center', fontweight='bold')
    
    # ========== BOTTOM: COMPOSITE STACKING ANALYSIS ==========
    
    ax.text(12, 1.2, 'POST-PROCESSING: COMPOSITE STACKING ANALYSIS', fontsize=12, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='#E0F2F1', edgecolor='#00695C', linewidth=2, pad=0.8))
    
    ax.text(12, 0.5, 
            'Stack all 18 horizon maps geographically | Count favorable horizons per location (threshold > 3.0) | Identify hotspots: 4-6 favorable horizons = Primary Targets (multi-pool play) | 1-2 favorable = Secondary (risky)',
            fontsize=9, ha='center', style='italic', color='#00695C', wrap=True)
    
    plt.tight_layout()
    plt.savefig('NGB_Workflow_Diagram_CORRECTED.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Saved: NGB_Workflow_Diagram_CORRECTED.png (300 DPI for publication)")
    plt.close()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("NORTH GERMAN BASIN: CORRECTED WORKFLOW DIAGRAM")
    print("Matching actual data structure from configuration table")
    print("="*70 + "\n")
    
    print("Generating corrected matplotlib version...")
    try:
        generate_workflow_diagram_corrected()
        print("\n" + "="*70)
        print("✓ DONE! File saved:")
        print("  • NGB_Workflow_Diagram_CORRECTED.png (300 DPI)")
        print("="*70 + "\n")
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
