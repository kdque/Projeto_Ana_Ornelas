<?php
class C {
    private string $C1;
    private int $C2;

    public function getC1(): string {
        return $this->C1;
    }

    public function setC1(string $C1): void {
        $this->C1 = $C1;
    }

    public function getC2(): int {
        return $this->C2;
    }

    public function setC2(int $C2): void {
        $this->C2 = $C2;
    }

    public function MC1() {
        echo "Método MC1()";
    }

    public function MC2() {
        echo "Método MC2()";
    }

    public function MC3() {
        echo "Método MC3()";
    }
}

