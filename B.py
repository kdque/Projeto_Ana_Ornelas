<?php
class B {
    private int $B1;
    private float $B2;

    public function getB1(): int {
        return $this->B1;
    }

    public function setB1(int $B1): void {
        $this->B1 = $B1;
    }

    public function getB2(): float {
        return $this->B2;
    }

    public function setB2(float $B2): void {
        $this->B2 = $B2;
    }

    public function MB1() {
        echo "Método MB1()";
    }

    public function MB2() {
        echo "Método MB2()";
    }
}
?>
