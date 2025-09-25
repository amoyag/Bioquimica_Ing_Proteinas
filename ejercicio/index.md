# Ejercicio: Rescate del Péptido β-Hairpin Disfuncional

## **Planteamiento del Problema**

Trabajas como ingeniero de proteínas. Un colega te ha enviado un péptido de 16 residuos con la siguiente secuencia:

**GEWTEDERTKTFTVTE**

Según tu colega:
- Este péptido fue diseñado para formar una estructura β-hairpin estable
- Se basó en los residuos 41-56 de la estructura PDB **1GB1**
- Sin embargo, los resultados experimentales muestran que el péptido se agrega en solución en lugar de plegarse en la estructura esperada
- Los intentos iniciales de plegamiento usando métodos computacionales también fallan en converger a un β-hairpin estable

**Tu misión:** Identifica por qué este péptido falla en plegarse correctamente y diseña una estrategia de rescate para restaurar su capacidad de formar β-hairpin.

---

## **Flujo de Trabajo Recomendado**

_Nota: El código mostrado no corresponde con funciones reales. Tómalo como código conceptual_

### **Fase 1: Investigación Estructural**

**1.1 Obtener la estructura de referencia**
```python
# Descargar y extraer el β-hairpin nativo desde 1GB1
pdb_file = download_pdb_structure("1GB1")
full_pose = pose_from_pdb(pdb_file) 
native_hairpin = extract_residue_range(full_pose, 41, 56)
```

**1.2 Comparar secuencias**
- Extraer la secuencia nativa de la estructura PDB
- Comparar con la secuencia problemática: `GEWTEDERTKTFTVTE`
- Identificar las mutaciones específicas que fueron introducidas
- Documentar qué posiciones cambiaron y a qué aminoácidos

**1.3 Análisis estructural inicial**
- Visualizar tanto la estructura nativa como la problemática
- Observar cualquier diferencia estructural obvia
- Prestar atención a la región del turn y las interacciones entre hebras

### **Fase 2: Análisis Diagnóstico**

**2.1 Análisis energético**
```python
# Comparar paisajes energéticos
analyze_energy_components(native_hairpin, "Nativa")
analyze_energy_components(problematic_hairpin, "Problemática")
```
- Identificar qué términos energéticos son más problemáticos
- Enfocarse en: fa_rep, fa_sol, fa_elec, hbond_sr_bb
- Determinar la penalización energética total de las mutaciones

**2.2 Evaluación del comportamiento de plegamiento**
```python
# Intentar plegamiento con Monte Carlo
folded_native = simple_monte_carlo_fold(native_hairpin, steps=1000)
folded_problematic = simple_monte_carlo_fold(problematic_hairpin, steps=1000)
```
- Comparar comportamiento de convergencia
- Analizar energías finales y estructuras
- Documentar por qué la variante problemática falla en plegarse

**2.3 Identificación de problemas estructurales**
- Mapear residuos problemáticos sobre la estructura 3D
- Identificar interacciones interrumpidas (hidrofóbicas, electrostáticas, puentes de hidrógeno)
- Analizar el impacto en la estabilidad de la estructura secundaria

### **Fase 3: Diseño de Rescate**

**3.1 Estrategia de diseño racional**
Basándote en tu análisis diagnóstico, propón mutaciones específicas para abordar:
- Choques electrostáticos o distribuciones de carga desfavorables
- Pérdida de interacciones del núcleo hidrofóbico
- Patrones de puentes de hidrógeno interrumpidos
- Preferencias de estructura secundaria

**3.2 Implementación usando PyRosetta**
```python
# Crear resfile con las mutaciones propuestas
resfile_content = """
NATRO
start
5 A PIKAA Q  # Ejemplo: neutralizar carga
7 A PIKAA T  # Ejemplo: restaurar residuo original
8 A PIKAA K  # Ejemplo: mantener mutación beneficiosa
"""

# Aplicar protocolo FastDesign

```

**3.3 Validación del diseño**
- Calcular mejoras energéticas
- Verificar que los términos energéticos problemáticos se reduzcan
- Comprobar que no se introducen nuevos problemas

### **Fase 4: Evaluación del diseño**

**4.1 Validación del plegamiento**
```python
# Probar plegamiento de la variante rescatada
rescued_folded = simple_monte_carlo_fold(rescued_hairpin, steps=1000)
```

**4.2 Análisis comparativo**
- Comparación energética: Nativa vs Original vs Rescatada
- Evaluación de similitud estructural
- Comparación del comportamiento de plegamiento

**4.3 Métricas de éxito**
Definir y evaluar criterios de éxito:
- ¿Se redujo la penalización energética en >50%?
- ¿Se restauró la convergencia del plegamiento?
- ¿La estructura final se asemeja al β-hairpin nativo?

---

## **Preguntas Clave a Abordar en tu Análisis**

1. **¿Qué mutaciones específicas causaron el fallo del plegamiento?**
   - ¿Qué residuos fueron cambiados?
   - ¿Qué propiedades químicas se alteraron?

2. **¿Cuáles son los factores desestabilizantes primarios?**
   - ¿Repulsión electrostática?
   - ¿Pérdida de interacciones hidrofóbicas?
   - ¿Disrupción de estructura secundaria?

3. **¿Qué estrategia de rescate es más apropiada?**
   - ¿Mutaciones conservativas (aminoácidos similares)?
   - ¿Reversión completa a la secuencia nativa?
   - ¿Soluciones alternativas que mantengan algunos cambios?

4. **¿Qué tan exitoso fue tu intento de rescate?**
   - ¿Mejoras energéticas cuantitativas?
   - ¿Evaluación estructural cualitativa?
   - ¿Factibilidad experimental predicha?

---

## **Requisitos del Entregable**

Entregar un análisis breve (1-2 páginas) que incluya:

**1. Identificación del Problema**
- Alineamiento de secuencias nativa vs problemática
- Mutaciones clave identificadas
- Factores desestabilizantes primarios

**2. Estrategia de Rescate** 
- Justificación de las mutaciones elegidas
- Impacto esperado en la estabilidad
- Enfoques alternativos considerados

**3. Resumen de Resultados**
- Tabla de comparación energética (Nativa/Problemática/Rescatada)
- Evaluación del comportamiento de plegamiento
- Conclusiones del análisis estructural

**4. Evaluación del Éxito**
- Métricas de éxito objetivas
- Limitaciones de tu enfoque
- Recomendaciones para validación experimental

---

## **Consejos**

- **Inicia sistemáticamente**: No saltes a soluciones sin entender el problema
- **Usa análisis cuantitativo**: Los números energéticos guían tus decisiones de diseño
- **Piensa químicamente**: Considera qué hace cada mutación al entorno químico local
- **Valida iterativamente**: Prueba tus diseños computacionalmente antes de reclamar éxito
- **Documenta todo**: Mantén registro de qué funciona y qué no
- **Haz preguntas**: Usa los recursos disponibles (documentación, asistentes IA...)

---

## **Para hacerlo más inrteresante (Opcional)**

- ¿Puedes rescatar con menos mutaciones de las que inicialmente propusiste?
- Diseña múltiples estrategias alternativas de rescate y compara su efectividad
- Analiza si tu rescate mantiene aspectos beneficiosos de las mutaciones originales
- Predice qué estrategia de rescate sería más factible experimentalmente

---

**Recuerda: Este ejercicio simula desafíos reales de ingeniería de proteínas. El éxito parcial sigue siendo aprendizaje valioso, y los resultados negativos nos enseñan lecciones importantes sobre las relaciones secuencia-estructura.**