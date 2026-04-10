package ejercicio1;

public class Fraccion {

    private int numerador;
    private int denominador;

    public Fraccion() {
        this.numerador = 0;
        this.denominador = 1;
    }

    public Fraccion(int n, int d) {
        this.numerador = n;
        this.denominador = d;
    }

    @Override
    public boolean equals(Object o) {
        if (o instanceof Fraccion) {
            Fraccion f = (Fraccion) o;
            return f.numerador == this.numerador &&
                   f.denominador == this.denominador;
        }
        return false;
    }

    @Override
    public String toString() {
        return this.numerador + "/" + this.denominador;
    }

    public Fraccion suma(Fraccion o) {
        int n = this.numerador * o.denominador + this.denominador * o.numerador;
        int d = this.denominador * o.denominador;
        return new Fraccion(n, d);
    }

    public Fraccion resta(Fraccion o) {
        Fraccion c = new Fraccion();
        c.numerador = this.numerador * o.denominador - this.denominador * o.numerador;
        c.denominador = this.denominador * o.denominador;
        return c;
    }

    public Fraccion multiplica(Fraccion o) {
        int n = this.numerador * o.numerador;
        int d = this.denominador * o.denominador;
        return new Fraccion(n, d);
    }

    public Fraccion divide(Fraccion o) {
        if (o.numerador == 0) {
            throw new ArithmeticException("No se puede dividir entre 0");
        }
        int n = this.numerador * o.denominador;
        int d = this.denominador * o.numerador;
        return new Fraccion(n, d);
    }

    public double convertirADecimal() {
        if (this.denominador == 0) {
            throw new ArithmeticException("División entre 0");
        }
        return (double) this.numerador / this.denominador;
    }

    public boolean esInverso(Fraccion o) {
        Fraccion r = this.multiplica(o);
        return r.numerador == r.denominador;
    }

    public static Fraccion parseFraccion(String str) {
        String[] partes = str.split("/");
        int n = Integer.parseInt(partes[0].trim());
        int d = Integer.parseInt(partes[1].trim());
        return new Fraccion(n, d);
    }

    public Fraccion simplifica() {
        int mcd = mcd(Math.abs(numerador), Math.abs(denominador));
        return new Fraccion(numerador / mcd, denominador / mcd);
    }

    private int mcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}