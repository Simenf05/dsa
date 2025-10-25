# Denne filen inneholder skjelettet til Oppgave 2 på Praktisk Øving 3 i TDT4160
j _tests

#
# rand er en funksjon som genererer pseudotilfeldige tall.
# De genererte tallene er 32 bits og returneres i registret a0.
# Merk at rand klusser til absolutt alle registre som ikke er ABI-bevart,
# og lagrer midlertidige verdier på stakken.
#
rand:
# Gjør plass for å lagre ra til stakken
addi sp, sp, -4
sw ra, 0(sp)

# Hent adressen til _rand_state
la t0, _rand_state
# Hent forrige _rand_state
lw t1, 0(t0)

# Oppdater rand state slik s_{i+1} = (a * s_i + c)
li t2, 1103515245 # a
li t3, 12345      # c

# Iterasjon 1
mul t4, t1, t2
add t5, t4, t3
# Iterasjon 2
mul t6, t5, t2
add a0, t6, t3
# Iterasjon 3
mul a1, a0, t2
add a2, a1, t3
# Iterasjon 4
mul a3, a2, t2
add a4, a3, t3
# Iterasjon 5
mul a5, a4, t2
add a6, a5, t3

# Lagrer den nye verdien av _rand_state
sw a6, 0(t0)

# Sett sammen minst signifikante byte fra iterasjonene 2 - 5
andi a0, a0, 255
andi a2, a2, 255
andi a4, a4, 255
andi a6, a6, 255
mv a7, a0
slli a7, a7, 8
or a7, a7, a2
slli a7, a7, 8
or a7, a7, a4
slli a7, a7, 8
or a7, a7, a6

# Returner den nye verdien
mv a0, a7

# Gjenoppretter den opprinnelige verdien til ra, og sp
lw ra, 0(sp)
addi sp, sp, 4
ret

########################################################################################
######################## Skriv koden din under denne linja #############################
########################################################################################

# Denne funksjonen skal fylle en liste med pseudotilfeldige 32-bits tall.
# Det første tallet i listen skal være resultatet av å kalle rand-funksjonen.
# Det neste tallet skal være resultatet av å kalle rand en gang til, osv.
# Register a0 er adressen til starten på listen
# Register a1 er lengden på listen
# Funksjonen returnerer ingenting
fill_random:

    # I denne oppgaven skal du kalle rand-funksjonen i en løkke.
    # Hvert kall til rand vil kludre til samtlige registre som ikke er ABI-bevarte.
    # Løkken din burde derfor bruke ABI-bevarte registre.
    # Før du bruker disse registrene må du lagre verdiene deres på stakken,
    # slik at du kan gjenopprette dem før du returnerer.
    # Husk å også gjenopprette stakk-pekeren (sp), og ikke kludre til stakken over sp.

    # TODO: Implementasjon

    # Forlater fill_random her
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

    la a0, _target
    li a1, 10
    call fill_random

    # Sjekker at listen ser ut som forventet
    la t0, _target
    la t1, _expected
    li t2, 0
    li t3, 10
_check_loop:
    beq t2, t3, _check_loop_done

    lw t4, 0(t0) # List value we got
    lw t5, 0(t1) # List value we expected
    bne t4, t5, _list_wrong

    addi t0, t0, 4
    addi t1, t1, 4
    addi t2, t2, 1
    j _check_loop

_check_loop_done:

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

_list_wrong:
    la a0, _list_wrong_str
    li a7, 4 # Print string
    ecall

    la a0, _list_wrong_got_str
    li a7, 4 # Print string
    ecall
    mv a0, t4
    li a7, 1 # Print int
    ecall

    la a0, _list_wrong_expected_str
    li a7, 4 # Print string
    ecall
    mv a0, t5
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

# Globale variabler
.data
_rand_state: .word 1

# Dette er stedet i minnet listen skal bli skrevet til
_target: .zero 40
# Dette er listen vi forventer å få
_expected:
    .word -409715406
    .word 3768031
    .word -175441128
    .word 1456981165
    .word 1932568878
    .word 1550138091
    .word -519649292
    .word -1838981095
    .word -1081289238
    .word 2018621111

_list_wrong_str: .string "Funksjonen produserte ikke riktig tall!"
_list_wrong_got_str:  .string "\nFikk: "
_list_wrong_expected_str:  .string "\nForventet: "
_abi_clobbered_str: .string "ABI-bevarte registre ble ikke bevart!"
_stack_clobbered_str: .string "Stakken ble ikke bevart!"
_all_tests_passed_str: .string "Testen var vellykket!"
