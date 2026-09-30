# KBR H2ACT® — Preliminary OSBL Equipment Sizing, 12 kTPA H₂

**Status:** Derived, preliminary (Gentari internal). **This is not a KBR deliverable.**
It sizes the items on KBR's OSBL equipment list from KBR's own utility, feed/product
and HMB figures. All KBR inputs are Rev 0 proposal-stage and indicative. Anything
not taken from KBR is tagged **[A#]** (a Gentari assumption) or cites a public
source. Treat every capacity below as a starting basis for EPC/FEED, not a
purchase specification.

- **Case:** 12 kTPA H₂, 100% NG fuel mode (the case KBR's HMB and utility summary cover),
  99.97 mol% H₂, Pasir Gudang, Johor
- **Equipment list sized:** `Licensor/kbr/I.H_GENTARIEquipment_List_OSBL_Rev0.md`
  (Gentari-PR-GEN-LST-0002, Rev 0, 23/12/2025)
- **Calculation:** `tools/kbr_osbl_sizing_12ktpa.py`. The calculated figures in the tables below come
  from that script, so rerun it after any change to an input.
- **Date:** 2026-09-30

> **Superseded for multi-capacity work (2026-09-30):** the Excel workbook
> `output/KBR_OSBL_Equipment_Sizing.xlsx` (build: `python tools/kbr_osbl_workbook.py`)
> covers 12, 24, 80 and 160 kTPA with live formulas. For consistency across capacities
> it takes the flare proxy and H₂ metering from **I.E** (all capacities) rather than
> I.C (12 kTPA only). At 12 kTPA that gives a flare of **11,319 kg/h** (I.E NH₃ feed
> 10,290 kg/h, highest-feed mode; this page shows ~10,000) and H₂ metering of
> **1,569 kg/h** (this page shows 1,579). Everything else at 12 kTPA agrees within rounding.

## KBR source documents

| Ref | Document | KBR Doc No. | Used for |
|---|---|---|---|
| **I.A** | Process Design Basis | Gentari-PR-GEN-PDB-001 | CW temps, ambient, NG pressure, turndown, H₂ delivery |
| **I.C** | Heat & Material Balance (12 kTPA, NG) | Gentari-PR-GEN-HMB-001 | NH₃ feed, H₂ product, NG fuel streams |
| **I.E** | Feed & Product Summary | Gentari-PR-GEN-F&F-001 | H₂ rate, NG LHV, power normal load |
| **I.F** | Utility Summary, ISBL (12 kTPA) | Gentari-PR-GEN-BLS-001 | **Main basis**: power, CW, demin, air, N₂, NG |
| **hub** | H2ACT® Technical Information Package | `kbr-johor-hub.md` | Blowdown effluent, per-t H₂ utility ratios, OSBL exclusions |

## Sizing rules

1. **Power, as instructed by the repo owner:** KBR's I.F maximum of 540 kW **× 2**, because
   I.F Note 7 says the figure covers ISBL process users only. It excludes cooling tower
   pumps and fans, the N₂ generator, lighting, buildings and instrumentation. The result
   gets 24 h of backup, a 50% engine efficiency and diesel LHV.
2. **Everything else:** the design flow is KBR's I.F **maximum** × 1.10 **[A1]**.
3. **Storage tanks:** **24 h** of autonomy at the design flow **[A2]**, the same philosophy
   as the 24 h diesel basis. Nominal volume = net volume ÷ 0.9 for heel and freeboard.
4. **Spares:** A/B pumps are 2 × 100% (duty/standby). A/B/C items are 3 × 50%
   (2 duty + 1 standby) **[A3]**.

## Assumptions register

| # | Assumption | Value | Why / where it applies |
|---|---|---|---|
| A1 | Design margin on KBR maximum flows | +10% | All pumps and packages except emergency power |
| A2 | Storage autonomy / net-to-nominal ratio | 24 h / 0.90 | All tanks. Extends the owner's 24 h diesel basis |
| A3 | Sparing | A/B = 2×100%; A/B/C = 3×50% | Pumps, compressors, CT cells |
| A4 | Power multiplier | ×2 on 540 kW | **Owner instruction** (I.F Note 7) |
| A5 | Genset efficiency / backup time | 50% / 24 h | **Owner instruction** |
| A6 | Cooling tower cycles of concentration | 5 | CT blowdown and make-up |
| A7 | Demin plant recovery (product ÷ feed) | 80% | Raw water to demin, neutralisation waste |
| A8 | Site headcount / simultaneous safety showers | 30 persons / 2 | Potable water. **Owner to confirm headcount** |
| A9 | IA dryer type / compressor discharge | Heatless, 15% purge / 8.5 barg | Air compressor capacity. Discharge is 1 bar above the 7.5 barg header |
| A10 | Receiver hold-up | IA: 15 min, 7.5 → 4.0 barg. Wet air: 2 min of compressor output | 192-D, 191-D |
| A11 | Duration of the start-up N₂ peak | 24 h | Liquid N₂ storage. KBR says the peak is TBC (I.F Note 6) |
| A12 | Max H₂ export line velocity | 20 m/s | Indicative pig launcher / line size |
| A13 | N₂ generator and air compressors are self-contained and air-cooled | — | Keeps OSBL cooling loads off the CW system |
| A14 | Governing flare case = full cracked-gas rate (NH₃ feed mass, fully cracked) | — | Proxy only. To be replaced by the relief study |

**Public constants:**
- Diesel LHV 43.0 MJ/kg (IPCC 2006 Guidelines Vol. 2 Ch. 1 Table 1.2, gas/diesel oil NCV 43.0 TJ/Gg)
- Diesel density 820 kg/m³. EN 590 allows 820–845 kg/m³ at 15 °C, and the low end gives the larger tank.
- Water cp 4.186 kJ/kg·K; latent heat 2,430 kJ/kg at 30 °C (steam tables)
- Liquid N₂ 806.6 kg/m³ at its normal boiling point; N₂ gas 1.2506 kg/Nm³ (0 °C, 1 atm) → 645 Nm³ of gas per m³ of liquid
- Safety shower 75.7 L/min (20 gpm) for 15 min (ANSI/ISEA Z358.1)
- Potable water 100 L/person/day, the upper end of the WHO/UN 50–100 L/p/d range
- Wet-bulb temperature from the Stull (2011) formula

---

## 1. Emergency power: worked example (owner's method)

| Step | Calculation | Result | Source |
|---|---|---|---|
| KBR max ISBL power | — | 540 kW | I.F, Electrical Power, "Maximum" column |
| Design power | 540 × 2 (Note 7 excludes OSBL users) | **1,080 kWe** | I.F Note 7; A4 |
| Apparent power | 1,080 ÷ 0.8 pf | **1,350 kVA** | Rated at 0.8 pf (standard genset rating basis) |
| Electrical energy, 24 h | 1,080 × 24 | 25,920 kWh | A5 |
| Fuel energy | 25,920 ÷ 0.50 = 51,840 kWh | 186,624 MJ | A5 (50% efficiency) |
| Diesel mass | 186,624 ÷ 43.0 MJ/kg | 4,340 kg | IPCC LHV |
| Burn rate | 4,340 ÷ 24 | 181 kg/h ≈ 221 L/h | — |
| Net diesel volume | 4,340 ÷ 820 kg/m³ | **5.3 m³** | EN 590 density |
| Nominal tank volume | 5.3 ÷ 0.9 | **≈ 5.9 m³ → specify 6 m³** | A2 |

> ⚠️ **Flag, KBR's own emergency figure is much smaller.** I.F **Note 9** says: *"Emergency
> backup power is estimated 0.3 MW for L.O. pumps for rotating equipment, instrumentation,
> MOVs, etc."* The owner's basis of 1,080 kWe is **3.6×** that. It sizes the genset to run
> the whole plant, including OSBL, rather than only for a safe shutdown. Both are valid
> philosophies, but they are different ones, so record which one was chosen. On KBR's
> 300 kW basis, the 24 h tank would be only **1.5 m³** net.
>
> **Efficiency sensitivity:** at 40% efficiency instead of 50%, the net diesel volume rises
> from 5.3 to **6.6 m³** (7.4 m³ nominal). Confirm the vendor's heat rate before fixing the
> tank size.

---

## 2. Sized equipment list: 12 kTPA H₂

The confidence column says how much the result rests on KBR data:
- **H** = mostly KBR data, little assumption
- **M** = KBR data plus material assumptions
- **L** = mostly assumptions
- **TBD** = cannot be sized from the available data

### Unit 101 — Emergency Power Generation / Sub-Station

| Tag | Item | Qty | Basis (KBR ref) | Design capacity | Conf. |
|---|---|---|---|---|---|
| 111-L | Emergency Power Package | 1 | 540 kW max × 2 (I.F, Note 7) | **1,080 kWe / 1,350 kVA @ 0.8 pf** | H (owner method) |
| 111-F | Emergency Power Diesel Tank | 1 | 24 h at 1,080 kWe, 50% efficiency, LHV 43.0 MJ/kg | **5.3 m³ net / 6 m³ nominal** (4,340 kg; 221 L/h burn) | H (owner method) |

### Unit 107 — Cooling Water System

Worked here first because the raw water sizing depends on the cooling tower make-up.

| Tag | Item | Qty | Basis (KBR ref) | Design capacity | Conf. |
|---|---|---|---|---|---|
| 171-JA/B/C | Cooling Water Pumps | 3 (2+1) | 40 t/h max (I.F, includes start-up coolers) × 1.1 | **44 m³/h total → 22 m³/h each**, ≥ 5.0 barg discharge (I.F) | H |
| 171-DA/B | Cooling Water Towers | 2 cells | 44 m³/h × 4.186 × ΔT 10 °C (30 → 40 °C, I.A §6 / I.D §6) | **512 kW total → 256 kW / 22 m³/h per cell**; 30 °C supply | M |
| — | CT evaporation / blowdown / make-up | — | Evaporation = duty ÷ 2,430 kJ/kg; COC 5 [A6] | Evaporation 758 kg/h; blowdown 189 kg/h; **make-up 947 kg/h** | M |
| 171-L | Chemical Injection Package | 1 | Make-up 0.95 m³/h; circulation 44 m³/h | Dosing rates by the water-treatment vendor | L |

> ⚠️ **CW supply temperature: the KBR documents conflict.** I.F gives 25 °C supply / 35 °C
> return. I.A §6 and I.D §6 give 30 °C / 40 °C. At I.A's design ambient of 28 °C and
> 80% RH, the wet bulb is **≈ 25.2 °C** (Stull), so a 25 °C supply is **below the wet bulb**
> and a cooling tower cannot deliver it. This sizing uses **30 °C** (a 4.8 °C approach).
> ΔT is 10 °C in both versions, so the duty is the same either way.
>
> Also, I.A's 28 °C / 80% is an annual average. A real CT design wet bulb should use a 1%
> exceedance value, which is higher and still needs to be obtained.

### Units 103 / 104 — Demineralised & Polished Water

This assumes the chain demin package → 131-F → mixed-bed polishing → 141-F → ISBL
boiler feed make-up at 5.0 barg (I.F). KBR's I.F treats the demin water import as a
single OSBL supply.

| Tag | Item | Qty | Basis (KBR ref) | Design capacity | Conf. |
|---|---|---|---|---|---|
| 131-L | Demineralised Water Package | 1 | 270 kg/h max (I.F) × 1.1 | **0.30 m³/h product** (0.37 m³/h raw feed at 80% recovery [A7]) | M |
| 131-F | Demineralised Water Tank | 1 | 24 h × 0.30 m³/h | **7.1 m³ net / 8 m³ nominal** | M |
| 131-JA/B | Demineralised Water Pumps | 2 (1+1) | 0.30 m³/h | **0.30 m³/h each** | M |
| 141-L | Mixed Bed Polishing Package | 1 | 0.30 m³/h | **0.30 m³/h** | M |
| 141-F | Polished Water Tank | 1 | 24 h × 0.30 m³/h | **7.1 m³ net / 8 m³ nominal** | M |
| 141-JA/B | Polished Water Pumps | 2 (1+1) | 0.30 m³/h at ISBL BL 5.0 barg (I.F) | **0.30 m³/h each, ≥ 5.0 barg at BL** | M |
| 132-F | Neutralization Tank | 1 | Regeneration/reject waste = 0.37 − 0.30 = 0.074 m³/h × 24 h | **1.8 m³ net / 2 m³ nominal** | L |
| 132-JA/B | Waste Water Pumps | 2 (1+1) | Transfer of 132-F contents | **≥ 0.074 m³/h** (vendor minimum will govern) | L |

The 0.30 m³/h demin package is very small, probably below a standard skid size. The
vendor will set the practical size. It also has to cover filling the steam system at
start-up, which KBR marks TBC in I.F Note 3.

### Unit 105 — Potable Water

| Tag | Item | Qty | Basis | Design capacity | Conf. |
|---|---|---|---|---|---|
| 151-F | Potable Water Tank | 1 | 30 persons × 100 L/day [A8] + 2 safety showers × 75.7 L/min × 15 min (ANSI Z358.1) | **5.3 m³ net / 6 m³ nominal** | L |
| 151-JA/B | Potable Water Pumps | listed as 1, see flag | 2 showers × 75.7 L/min + 3 × average domestic flow | **9.5 m³/h each** | L |
| 151-L | Chlorination Package | 1 | Dose the tank fill to ≥ 0.5 mg/L free Cl₂ after ≥ 30 min contact (WHO GDWQ) | Sized to the fill rate, ~0.13 m³/h average | L |

No KBR input exists for this unit. Headcount and the safety-shower philosophy are owner
inputs. A chlorination-only package also assumes the raw water is already of
municipal quality, which needs confirming.

### Unit 102 — Raw Water

| Tag | Item | Qty | Basis | Design capacity | Conf. |
|---|---|---|---|---|---|
| 121-F | Raw Water Tank | 1 | 24 h × (CT make-up 0.95 + demin feed 0.37 + potable 0.13 m³/h) = 1.44 m³/h | **34.7 m³ net / ~40 m³ nominal, plus the fire water reserve (TBD, see Unit 106)** | M |
| 121-JA/B | Service Water Pumps | 2 (1+1) | 1.44 m³/h continuous | **≥ 1.5 m³/h each**, plus a utility hose station allowance (TBD) | M |

### Unit 106 — Fire Water

| Tag | Item | Qty | Basis | Design capacity | Conf. |
|---|---|---|---|---|---|
| 161-JA/B | Fire water pumps (labelled "Service Water Pumps" in I.H) | 2 | No KBR data. Needs a Fire & Explosion Risk Assessment and the local authority's requirement | **TBD** | TBD |

Unit 106 has no fire water tank of its own. That suggests the **fire water reserve is held
in 121-F**, a common shared raw/fire water tank arrangement. If so, 121-F = 40 m³ plus
(fire water rate × required duration), and the fire reserve will almost certainly
dominate the tank size. If one of the fire pumps is diesel-driven, which is typical
practice, it also needs its own day tank, and that is not on the I.H list.

### Unit 108 — Ammonia Cracking Flare & Fuel Gas System

| Tag | Item | Qty | Basis (KBR ref) | Design capacity | Conf. |
|---|---|---|---|---|---|
| 181-L | HP Flare Package | 1 | Proxy governing case [A14]: full cracked gas = NH₃ feed 9,104 kg/h (I.C stream 1), 2 mol out per mol NH₃ | **≈ 10,000 kg/h ≈ 26,200 Nm³/h, MW ≈ 8.5** (H₂/N₂ 3:1) | L |
| 181-D | HP Flare KO Drum | 1 | Same load. Dimension to API Std 521 droplet separation at FEED | **10,000 kg/h gas basis** | L |
| 181-C | HP Flare KO Drum Heater | 1 | Depends on liquid inventory (NH₃/water). No KBR data | **TBD** | TBD |
| 182-L | Fuel Gas Metering Package | 1 | NG max 450 kg/h (I.F, covers start-up per Note 10) × 1.1; MW 16.95 (I.C stream 13) | **495 kg/h ≈ 655 Nm³/h ≈ 6.8 MW (LHV)** at 7.5 barg (I.F) | H |
| 182-D | Fuel Gas KO Drum | 1 | Same as 182-L | **495 kg/h ≈ 655 Nm³/h** | H |

The flare figure is a placeholder upper bound until KBR or the EPC supplies the relief
load summary. Blocked H₂ export alone would be only ~1,435 kg/h (I.C stream 8).

### Unit 109 — Air Systems

| Tag | Item | Qty | Basis (KBR ref) | Design capacity | Conf. |
|---|---|---|---|---|---|
| 191-JA/B/C | Air Compressor Package | 3 (2+1) | PA 250 × 1.1 + IA dryer inlet 453 (I.F max; A9) | **728 Nm³/h total → 364 Nm³/h each**, ≥ 8.5 barg discharge | M |
| 191-D | Wet Air Receiver | 1 | 2 min of 728 Nm³/h, 7.5 → 4.0 barg [A10] | **≈ 7 m³** | L |
| 191-L | Instrument Air Dryer Package | 1 | IA 350 (I.F max) × 1.1 | **385 Nm³/h dry product** (453 Nm³/h inlet); dew point spec TBD | M |
| 192-D | Instrument Air Receiver | 1 | 15 min of IA 350 Nm³/h, 7.5 → 4.0 barg [A10] | **≈ 25 m³** | M |

I.F Note 8 says the KBR air figures are reference-plant estimates.

### Unit 110 — Nitrogen System

| Tag | Item | Qty | Basis (KBR ref) | Design capacity | Conf. |
|---|---|---|---|---|---|
| 201-L | Nitrogen Generation Package | 1 | Normal 150 Nm³/h (I.F) × 1.1 | **165 Nm³/h at ≥ 7.0 barg** (I.F). Purity not stated by KBR, TBD | M |
| 201-D | Liquid Nitrogen Storage Vessel | 1 | Start-up peak 500 Nm³/h (I.F) less the generator's 165 = 335 Nm³/h × 24 h [A11] ÷ 645 | **12.5 m³ LN₂ net / 14 m³ nominal** | L |
| 201-CA/B | Nitrogen Ambient Vaporisers | 2 (2×100%, alternating for defrost) | Peak 500 Nm³/h (I.F) × 1.1 | **550 Nm³/h each** | M |

KBR says the peak N₂ quantity and duration are TBC (I.F Notes 5–6). The 24 h is the
main driver of the 201-D size, so confirm it with KBR.

### Unit 111 — Off-Spec Tank

| Tag | Item | Qty | Basis | Design capacity | Conf. |
|---|---|---|---|---|---|
| 211-F | Off-Spec Tank | 1 | Service not defined by KBR: off-spec liquid NH₃ or aqueous ammonia? | **TBD**. Ask KBR for the service and the inventory to be received | TBD |

### Unit 112 — Waste Water Treatment

| Tag | Item | Qty | Basis (KBR ref) | Design capacity | Conf. |
|---|---|---|---|---|---|
| 221-JA/B | Neutralization Sump Pump | 2 (1+1) | Demin regeneration/reject waste 0.074 m³/h [A7] | **≥ 0.074 m³/h**. Possibly the same service as 132-JA/B, see flag | L |
| 221-L | Oil Water Treatment Package | 1 | Oily storm water from paved process area. Needs rainfall intensity and paved area | **TBD** | TBD |
| 222-L | Sanitary Lifting Station | 1 | Equal to potable use: 3 m³/d [A8] | **3 m³/d (~0.13 m³/h average)** | L |
| 222-JA/B | Waste Water Effluent Sump Pump | 2 (1+1) | Continuous effluent = steam blowdown 86 kg/h (hub §3.5, < 0.06 t/t H₂) + CT blowdown 189 + demin waste 74 kg/h | **≥ 0.35 m³/h continuous, plus storm water (TBD, will dominate)** | M |

### Unit 113 — Hydrogen Export

| Tag | Item | Qty | Basis (KBR ref) | Design capacity | Conf. |
|---|---|---|---|---|---|
| 232-L | Hydrogen Metering Package | 1 | H₂ product 1,435 kg/h / 15,890 Nm³/h (I.C stream 8) × 1.1; 40% turndown (I.A §9) | **1,579 kg/h ≈ 17,480 Nm³/h ≈ 713 Am³/h at 27 barg / 30 °C**. Minimum 574 kg/h, so meter turndown ≥ 3:1 | H |
| 231-L | Hydrogen Pipeline Pig Launcher Package | 1 | Matches the export line size. At ≤ 20 m/s [A12] the minimum ID is 112 mm | **Indicative DN150 (6") line**, ~10.6 m/s at design flow. Final size follows the pipeline hydraulics | L |

### Unit 114 — Ammoniacal Water Drain System

| Tag | Item | Qty | Basis | Design capacity | Conf. |
|---|---|---|---|---|---|
| 241-D | Ammoniacal Drain Underground Drum | 1 | Largest ISBL ammoniacal inventory drained at maintenance (e.g. HP Ammonia Scrubber 324-D, distillation column). Inventories not in the KBR package | **TBD** | TBD |
| 241-JA/B | Submerged Ammoniacal Drain Drum Pump | 2 (1+1) | Empty 241-D within a set time | **TBD** | TBD |

---

## 3. Power cross-check on the ×2 basis

The ×2 factor adds a 540 kW allowance for users outside I.F. The OSBL rotating loads
that can be estimated from this sizing are:

- Air compressors: ≈ 71 kW shaft (isothermal work to 8.5 barg at 65% isothermal
  efficiency, a cross-check assumption)
- CW pumps: ≈ 10 kW (5.5 bar ΔP, 70% efficiency)

Together that is **≈ 80 kW**. N₂ generation, CT fans, lighting and buildings are not
estimated here. Even allowing generously for them, **the ×2 basis looks conservative for
12 kTPA**, which is consistent with the flag in §1.

## 4. Discrepancies found in the KBR package (flagged, not reconciled)

| # | Item | Source A | Source B | Used here |
|---|---|---|---|---|
| 1 | Emergency power | Owner basis 540 × 2 = 1,080 kW | I.F Note 9: ~0.3 MW | Owner basis, with KBR's figure shown as a sensitivity |
| 2 | CW supply/return temperature | I.F: 25 / 35 °C | I.A §6, I.D §6: 30 / 40 °C | 30 / 40 °C, since 25 °C is below the design wet bulb |
| 3 | CW supply/return pressure | I.F: 5.0 / 3.5 barg | I.A §6: 2.0 supply / 4.0 return (return higher than supply, which looks inverted). I.D §6: 4.0 barg supply | 5.0 barg (I.F, the highest) for pump discharge |
| 4 | CW normal flow | I.F: 30.1 t/h | hub §3.3: 25 t/t H₂ × 1.426 t/h = 35.7 t/h | I.F max of 40 t/h, which covers both |
| 5 | Demin make-up | I.F: 245 kg/h normal | hub §3.3: 0.1 t/t H₂ × 1.426 = 143 kg/h | I.F max of 270 kg/h (conservative) |
| 6 | NG supply pressure | I.F: 7.5 barg | I.A §5: 7 barg | 7.5 barg |
| 7 | H₂ product rate | I.C: 1,435 kg/h | I.E: 1,426 kg/h | I.C (higher) |
| 8 | H₂ delivery pressure | I.E / I.C: 27 barg | I.A: 20 barg minimum; hub §3.3: 28 barg (already open in memory.md) | 27 barg (the HMB) for metering |
| 9 | 161-JA/B description | I.H: "Service Water Pumps" under Unit 106 Fire Water | — | Treated as fire water pumps |
| 10 | 151-JA/B quantity | I.H: quantity 1 | Tag implies an A/B pair | Sized per pump; recommend 2 |
| 11 | 132-JA/B vs 221-JA/B | Both appear to handle neutralisation waste | — | Both sized on the same stream; confirm whether one is redundant |

## 5. Owner inputs still needed to close the TBDs

1. Fire water design rate and duration (FERA / local authority) → 161-JA/B and the fire reserve in 121-F
2. Site headcount and safety-shower philosophy → Unit 105, 222-L
3. Relief load summary (KBR/EPC) → 181-L, 181-D, 181-C
4. Off-spec tank service and inventory (KBR) → 211-F
5. ISBL ammoniacal drain inventories (KBR) → 241-D, 241-JA/B
6. Rainfall intensity and paved area → 221-L, 222-JA/B
7. N₂ start-up peak duration and purity (KBR I.F Notes 5–6) → 201-D, 201-L
8. Confirmed genset heat rate and emergency power philosophy (full plant vs. safe-shutdown) → 111-L, 111-F
