# 42_Notes_FQ01_P26_SdF_annoté.pdf readable notes

- Source: `42_Notes_FQ01_P26_SdF_annoté.pdf`
- Final-exam priority: P0
- Role: Handwritten annotated SdF TD notes. Use with `43_FQ01_TD_Correction.readable.txt`, SdF CM PDF, and SdF TD/CM ASR.
- Conversion method: manual structural transcription from rendered pages because the PDF is Xournal++ handwritten/annotated content and `pdftotext` extracts no useful text.
- Uncertainty: some handwriting symbols are visually inferred. Formula structure and exam-useful steps are preserved; for exact official wording, prefer `43_FQ01_TD_Correction.readable.txt`.

## Page 1 - Disponibilite a(t): small time-step decomposition

Context: two repairable components `C1`, `C2` in parallel. Parameters:

- Failure rate: `lambda > 0`.
- Repair rate: `mu > 0`.
- `a(t) = P(component in working state at time t)`.

Goal:

```text
a(t + dt) = g(a(t))
```

Use total probability by conditioning on the state at time `t`:

```text
a(t + dt)
= P(component working at t + dt)
= P(working at t + dt, working at t)
  + P(working at t + dt, failed at t)
= P1 + P2
```

Term `P1`: component is working at `t`, and remains working until `t + dt`.

```text
P1 = P(working at t + dt | working at t) P(working at t)
```

With exponential lifetime and no-memory property:

```text
P(working at t + dt | working at t)
= P(working at dt | working at 0)
= R(dt)
= exp(-lambda dt)
≈ 1 - lambda dt
```

Therefore:

```text
P1 ≈ (1 - lambda dt) a(t)
```

Term `P2`: component is failed at `t`, and repair is completed before `t + dt`.

```text
P2 = P(working at t + dt | failed at t) P(failed at t)
```

With exponential repair time and no-memory property:

```text
P(working at t + dt | failed at t)
= P(working at dt | failed at 0)
= m(dt)
= 1 - exp(-mu dt)
≈ mu dt
```

Since `P(failed at t) = 1 - a(t)`:

```text
P2 ≈ mu dt (1 - a(t))
```

Main recurrence:

```text
a(t + dt) = (1 - lambda dt) a(t) + mu dt (1 - a(t))
```

Expanded form:

```text
a(t + dt) = a(t) - lambda dt a(t) + mu dt - mu dt a(t)
```

## Page 2 - Differential equation and solution method

Starting from:

```text
a(t + dt) = a(t) - lambda dt a(t) + mu dt - mu dt a(t)
```

Move `a(t)` and divide by `dt`:

```text
[a(t + dt) - a(t)] / dt = mu - (lambda + mu) a(t)
```

Taking the limit `dt -> 0`:

```text
a'(t) = mu - (lambda + mu) a(t)
```

Equivalent first-order linear differential equation:

```text
a'(t) + (lambda + mu) a(t) = mu
```

Homogeneous solution:

```text
a'_h(t) = -(lambda + mu) a_h(t)
a'_h(t) / a_h(t) = -(lambda + mu)
ln(a_h(t)) = -(lambda + mu)t + C
a_h(t) = K exp(-(lambda + mu)t)
```

Non-homogeneous solution by variation of constant:

```text
a(t) = K(t) exp(-(lambda + mu)t)
```

Derivative:

```text
a'(t) = K'(t) exp(-(lambda + mu)t)
        - (lambda + mu) K(t) exp(-(lambda + mu)t)
```

Substitute into the differential equation:

```text
K'(t) exp(-(lambda + mu)t) = mu
K'(t) = mu exp((lambda + mu)t)
```

Integrate:

```text
K(t) = [mu / (lambda + mu)] exp((lambda + mu)t) + B
```

General solution:

```text
a(t) = B exp(-(lambda + mu)t) + mu / (lambda + mu)
```

## Page 3 - Initial condition and system availability for two parallel components

Initial condition:

```text
a(0) = 1
```

Apply to the general solution:

```text
B exp(0) + mu / (lambda + mu) = 1
B = 1 - mu / (lambda + mu)
B = lambda / (lambda + mu)
```

Single-component instantaneous availability:

```text
a(t) = [lambda / (lambda + mu)] exp(-(lambda + mu)t)
       + mu / (lambda + mu)
```

Two identical independent repairable components in parallel:

```text
A(t) = P(system working at t)
     = 1 - P(system failed at t)
     = 1 - P(C1 failed at t and C2 failed at t)
     = 1 - P(C1 failed at t) P(C2 failed at t)
```

With identical components:

```text
a1(t) = a2(t) = a(t)
A(t) = 1 - (1 - a(t))^2
A(t) = 2a(t) - a(t)^2
```

Substitute `a(t)`:

```text
1 - a(t) = [lambda / (lambda + mu)] [1 - exp(-(lambda + mu)t)]
```

Therefore:

```text
A(t) = 1 - [lambda^2 / (lambda + mu)^2] [1 - exp(-(lambda + mu)t)]^2
```

Asymptotic availability:

```text
a_infty = lim a(t) = mu / (lambda + mu)

A_infty = lim A(t)
        = 1 - lambda^2 / (lambda + mu)^2
        = [(lambda + mu)^2 - lambda^2] / (lambda + mu)^2
        = mu(2lambda + mu) / (lambda + mu)^2
```

Comparison noted in handwriting:

```text
A_infty > a_infty = mu / (lambda + mu)
```

## Page 4 - Maintainability and reliability improvement strategy

For two repairable components in parallel, system maintainability:

```text
M(t) = 1 - M_bar(t)
```

Interpreted as:

```text
M(t) = 1 - P(system failed at 0 and not yet repaired over [0, t])
```

For two components, both not repaired over `[0,t]`:

```text
M(t) = 1 - P(components 1 and 2 not repaired over [0,t])
     = 1 - M_bar(t)^2
     = 1 - exp(-2mu t)
```

Mean time to repair:

```text
MTTR = ∫_0^∞ M_bar(t) dt
     = ∫_0^∞ exp(-2mu t) dt
     = 1 / (2mu)
```

Reliability block exercise:

- Three blocks in series: `R = R1 R2 R3`.
- Initial reliabilities: `r1 = 0.9`, `r2 = 0.8`, `r3 = 0.5`.
- Initial system reliability:

```text
R0 = 0.9 * 0.8 * 0.5 = 0.36
```

Target:

```text
R >= 0.8
```

Strategy written in notes:

```text
Renforcer le bloc des composants le moins fiable.
```

Meaning: add redundant identical components in parallel first to the least reliable block.

For `n` identical parallel components each with reliability `r`, block reliability is:

```text
R_block = 1 - (1 - r)^n
```

Example table inferred from handwriting:

| n1 | n2 | n3 | R1 | R2 | R3 | R | decision |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 0.9 | 0.8 | 0.5 | 0.36 | add one C3 |
| 1 | 1 | 2 | 0.9 | 0.8 | 0.75 | 0.54 | add one C3 |
| 1 | 1 | 3 | 0.9 | 0.8 | 0.875 | 0.63 | add one C2 |
| 1 | 2 | 3 | 0.9 | 0.96 | 0.875 | 0.756 | add one C3 |
| 1 | 2 | 4 | 0.9 | 0.96 | 0.9375 | 0.81 | stop |

Exam conclusion:

```text
Choose n1 = 1, n2 = 2, n3 = 4 to obtain R ≈ 0.81 >= 0.8.
```

## Page 5 - Availability with component C3 state decomposition

The page studies a system with five components and component availabilities:

```text
a1(t), a2(t), ..., a5(t), A(t)
```

The diagram is decomposed according to the state of component `C3`.

If `C3` is failed at time `t`, the remaining structure is transformed into two branches:

```text
top branch: C1 then C4
bottom branch: C2 then C5
```

Availability conditional on `C3` failed:

```text
A3_bar(t) = P(system working at t | C3 failed at t)
           = 1 - (1 - a1(t)a4(t))(1 - a2(t)a5(t))
```

If `C3` is working at time `t`, the page indicates a different reduced structure. The final decomposition uses total probability:

```text
A(t) =
  P(system working at t | C3 failed at t) P(C3 failed at t)
  + P(system working at t | C3 working at t) P(C3 working at t)
```

Using:

```text
P(C3 failed at t) = 1 - a3(t)
P(C3 working at t) = a3(t)
```

The notes write:

```text
A(t) = A3_bar(t) [1 - a3(t)] + A3(t) a3(t)
```

where:

- `A3_bar(t)` is the equivalent availability of the system when `C3` is failed.
- `A3(t)` is the equivalent availability of the system when `C3` is working.

Uncertainty: the bottom green diagrams are schematic reductions; use the official correction if a full algebraic expression for `A3(t)` is needed.
