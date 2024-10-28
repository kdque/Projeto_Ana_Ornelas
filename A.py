<?php
class A {
    private int $A1;
    private float $A2;

    public function getA1(): int {
        return $this->A1;
    }

    public function setA1(int $A1): void {
        $this->A1 = $A1;
    }

    public function getA2(): float {
        return $this->A2;
    }

    public function setA2(float $A2): void {
        $this->A2 = $A2;
    }

    public function MA1() {
        echo "Método MA1()";
    }

    public function MA2() {
        echo "Método MA2()";
    }
}
?>
