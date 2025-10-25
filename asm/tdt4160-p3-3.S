# Denne filen inneholder skjelettet til Oppgave 3 på Praktisk Øving 3 i TDT4160
j _tests

########################################################################################
######################## Skriv koden din under denne linja #############################
########################################################################################

# Denne funksjonen tar inn en peker til en node i en binær trestruktur.
# Hver node ser slik ut:
#
# Byte offset:
# 0              4               8              12
# +--------------+---------------+--------------+
# | verdi        | venstre peker |  høyre peker |
# +--------------+---------------+--------------+
#
# der venstre og høyre peker er pekere til henholdsvis nodens venstre og høyre barn.
# Dersom noden ikke har en barn-node i en gitt retning, er pekeren 0.
#
# Når funksjonen kalles ligger en peker til rotnoden i register a0.
# Funksjonen skal regne ut summen av alle nodene i treet, og returnere svaret i register a0.
sum_binary_tree:

    # I denne oppgaven skal du ikke kalle noen funksjoner.
    # I stedet skal du bruke stakken for å holde orden på noder som gjenstår å besøke.
    # Funksjoner står fritt til å utvide stakken når de trenger midlertidig lagringsplass.
    # Dette er praktisk i denne funksjonen, siden vi ikke vet på forhånd hvor mye plass vi trenger.

    # For å dytte en 32-bits verdi fra t0 på stakken kan du bruke sekvensen:
    #
    #   addi sp, sp, -4
    #   sw t0, 0(sp)
    #
    # For å poppe av en 32-bits verdi fra stakken kan du bruke skvensen:
    #
    #   lw t0, 0(sp)
    #   addi sp, sp, 4

    # Pseudokode for hele funksjonen blir derfor:
    #
    #     sum = 0
    #     push rotnoden
    #     while (vi har flere noder på stakken):
    #          node = pop en node fra stakken
    #          sum += node.verdi
    #          if node.venstre != 0:
    #              push node.venstre
    #          if node.høyre != 0:
    #              push node.høyre
    #
    #     return sum
    #

    # Tips: For å gjøre det lett å oppdage når stakken er tom for noder
    # kan man dytte tallet 0 til stakken før vi begynner.
    # Da vet vi at vi er ferdige så snart vi popper 0.

    # Som vanlig må du passe på å ikke kludre til ABI-bevarte registre,
    # passe på at stakk-pekeren (sp) ender opp tilbake der den begynte,
    # og at ingen av verdiene som ligger over sp på stakken er blitt overskrevet.

    # Forlater sum_binary_tree her
    ret

########################################################################################
######################## Skriv koden din over denne linja ##############################
########################################################################################

_tests:
    # Setter ABI-bevarte registre til 77
    li s0, 77
    li s1, 77
    li s2, 77
    li s3, 77
    li s4, 77
    li s5, 77
    li s6, 77
    li s7, 77
    li s8, 77
    li s9, 77
    li s10, 77
    li s11, 77

    # Skriver 4 stykk 77 til stakken
    addi sp, sp, 16
    sw s0, 0(sp)
    sw s0, 4(sp)
    sw s0, 8(sp)
    sw s0, 12(sp)

    la a0, _node0
    call sum_binary_tree

    # Sjekker at summen ble som forventet
    mv t0, a0
    lw t1, _expected_sum
    bne t0, t1, _sum_wrong

    # Sjekker at ingen av de ABI-bevarte registrene har blitt tuklet med
    li t0, 77
    bne s0, t0, _abi_clobbered
    bne s1, t0, _abi_clobbered
    bne s2, t0, _abi_clobbered
    bne s3, t0, _abi_clobbered
    bne s4, t0, _abi_clobbered
    bne s5, t0, _abi_clobbered
    bne s6, t0, _abi_clobbered
    bne s7, t0, _abi_clobbered
    bne s8, t0, _abi_clobbered
    bne s9, t0, _abi_clobbered
    bne s10, t0, _abi_clobbered
    bne s11, t0, _abi_clobbered

    # Sjekker at sp er på riktig sted og stakken er bevart
    lw t1, 0(sp)
    lw t2, 4(sp)
    lw t3, 8(sp)
    lw t4, 12(sp)
    bne t1, t0, _stack_clobbered
    bne t2, t0, _stack_clobbered
    bne t3, t0, _stack_clobbered
    bne t4, t0, _stack_clobbered

    j _all_tests_passed

_sum_wrong:
    la a0, _sum_wrong_str
    li a7, 4 # Print string
    ecall

    la a0, _sum_wrong_got_str
    li a7, 4 # Print string
    ecall
    mv a0, t0
    li a7, 1 # Print int
    ecall

    la a0, _sum_wrong_expected_str
    li a7, 4 # Print string
    ecall
    mv a0, t1
    li a7, 1 # Print int
    ecall

    j _abort

_abi_clobbered:
    la a0, _abi_clobbered_str
    li a7, 4 # Print string
    ecall
    j _abort

_stack_clobbered:
    la a0, _stack_clobbered_str
    li a7, 4 # Print string
    ecall
    j _abort

_abort:
    # Exit med kode 1
    li a0, 1
    li a7, 93
    ecall

_all_tests_passed:
    la a0, _all_tests_passed_str
    li a7, 4 # Print string
    ecall

    # Exit med kode 0
    li a7, 10
    ecall

.data
# Treet som brukes i testing
_node7:  .word 7, , 0
.zero 16 # Dummy padding
_node6:  .word 3, 0, _node7
_node5:  .word 8, 0, _node6
_node4:  .word 2, 0, 0
_node3:  .word 9, _node4, 0
.zero 4 # Dummy padding
_node2:  .word 3, 0, 0
_node1:  .word 4, _node2, _node3
# Rotnoden
_node0: .word 6, _node1, _node5

_expected_sum:  .word 42

_sum_wrong_str: .string "Funksjonen produserte ikke riktig sum!"
_sum_wrong_got_str:  .string "\nFikk: "
_sum_wrong_expected_str:  .string "\nForventet: "
_abi_clobbered_str: .string "ABI-bevarte registre ble ikke bevart!"
_stack_clobbered_str: .string "Stakken ble ikke bevart!"
_all_tests_passed_str: .string "Testen var vellykket!"
