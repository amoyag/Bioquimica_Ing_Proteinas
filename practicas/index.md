## Estabilización térmica de cold shock proteins

### **Contexto Científico**

La termoestabilidad proteica es una propiedad crítica en biotecnología industrial, donde las enzimas deben funcionar a temperaturas elevadas. Comprender las bases moleculares de la estabilidad térmica permite diseñar proteínas más robustas para aplicaciones industriales, terapéuticas y de investigación.

Las *cold shock proteins* (Csps) son proteínas pequeñas (~70 residuos) que se encuentran en bacterias de todos los rangos térmicos: psicrófilas, mesófilas, termófilas e hipertermófilas. A pesar de su estructura tridimensional altamente conservada (β-barrel de 5 hebras), estas proteínas exhiben temperaturas de melting (Tm) que varían dramáticamente—desde 40°C en psicrófilas hasta >90°C en termófilas. Este sistema representa un modelo ideal para estudiar los determinantes estructurales de la termoestabilidad.

---

### **El Reto**

Trabajaréis en **equipos de 4 personas** para diseñar mutaciones que aumenten la estabilidad térmica de **Bs-CspB**, la proteína cold shock B de *Bacillus subtilis* (bacteria mesófila, Tm = 48°C).

**Objetivo:** Diseñar entre 1 y 10 mutaciones aproximadamente que maximicen la termoestabilidad predicha computacionalmente.


La **estructura 3D de Bs-CspB** de partida está en PDB: 1CSP. Su Tm es de 49 C (pH 7.0). No contiene puentes disulfuro, residuos cis-Pro ni cofactores unidos.


Un diseño se considera exitoso si:

1. **ΔΔG(diseño - WT_relajado) < -2.0 REU**
   - El diseño debe ser al menos 2 REU más estable que Bs-CspB WT
   - Nota: La variante termófila natural tiene ΔΔG ≈ -4 REU

2. **∆fa_rep < +20 REU** respecto a WT relajado
   - El término repulsivo no debe aumentar excesivamente

3. **Mantiene estructura general**
   - El plegamiento β-barrel debe conservarse

4. **Está científicamente justificado**
   - Cada mutación debe estar racionalmente fundamentada



**Nota técnica:** La energía por residuo individual puede ser engañosa.
Mutaciones que parecen desfavorables aisladamente pueden estabilizar
globalmente mediante interacciones de largo alcance. Siempre analizar el ΔΔG total de la proteína.


---


### **Sistema de Evaluación Competitiva**

Se evaluarán **dos dimensiones**:

#### **1. Estabilización Predicha (70%)**

Calculada como:
```
Score_estabilidad = ΔΔG_calculado × factor_eficiencia
```

Donde:
- `ΔΔG_calculado` = diferencia energética total (REU) respecto a WT
- `factor_eficiencia` = penalización por número de mutaciones:
  - 1 - 3  mutaciones: factor = 1.0
  - 4 - 6 mutaciones: factor = 0.9
  - 7 - 10 mutaciones: factor = 0.8
  - Más de 10 mutaciones: factor = 0.6
  

**Bonificación:** +5% si el diseño introduce al menos un salt bridge nuevo

#### **2. Calidad Científica (30%)**

- **Justificación del diseño (20%):** Razonamiento estructural y termodinámico
- **Análisis de resultados (15%):** Interpretación de métricas computacionales
- **Conexión con literatura (5%):** Uso de conceptos de termoestabilidad


---

### **Entregables**

Informe en formato de cuaderno jupyter

---

### **Recursos y Referencias**


1. **Robertson, A.D. & Murphy, K.P.** (1997) Protein structure and the energetics of protein stability. *Chem. Rev.* 97, 1251-1267.
   - Relación entre ΔΔG y Tm: ~0.008 kJ/(mol·residuo·K)

2. **Vieille, C. & Zeikus, G.J.** (2001) Hyperthermophilic enzymes: sources, uses, and molecular mechanisms for thermostability. *Microbiol. Mol. Biol. Rev.* 65, 1-43.
   - Revisión exhaustiva de estrategias moleculares de termoestabilidad

3. **Kumar, S., Tsai, C.J. & Nussinov, R.** (2000) Factors enhancing protein thermostability. *Protein Eng.* 13, 179-191.
   - Salt bridges, packing, rigidez de loops, puentes disulfuro



---

### **Correlación ΔΔG-Tm (Información Técnica)**

Estudios termodinámicos muestran que un incremento en estabilidad de ~0.008 kJ/(mol·residuo) está asociado, en promedio, con un aumento de 1°C en Tm.

**Para Bs-CspB (67 residuos) con estructuras relajadas:**
```
ΔTm (°C) ≈ 7.1 × ΔΔG (kcal/mol)
```

**Ejemplo:** Si PyRosetta predice ΔΔG = -2 REU (más estable), esto correspondería aproximadamente a ΔTm ≈ +14°C.

**Limitación importante:** Esta es una correlación empírica aproximada válida para cambios pequeños (< 10 mutaciones). PyRosetta calcula ΔG a temperatura de referencia, no Tm directamente.
