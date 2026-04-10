package ejercicio1;

public class TestFraccion {

    public static void main(String[] args) {

        Fraccion f1 = new Fraccion(1, 4);
        Fraccion f2 = new Fraccion(4, 3);

        System.out.println("f1 = " + f1);
        System.out.println("f2 = " + f2);

        System.out.println("\n--- OPERACIONES ---");
        System.out.println("suma = " + f1.suma(f2));
        System.out.println("resta = " + f1.resta(f2));

        System.out.println("\n--- INCISO a) MULTIPLICACIÓN ---");
        System.out.println(f1 + " * " + f2 + " = " + f1.multiplica(f2));

        System.out.println("\n--- INCISO b) DIVISIÓN ---");
        System.out.println(f1 + " / " + f2 + " = " + f1.divide(f2));

        System.out.println("\n--- INCISO c) DECIMAL ---");
        System.out.println(f1 + " = " + f1.convertirADecimal());

        System.out.println("\n--- INCISO d) INVERSO ---");
        System.out.println("¿" + f1 + " es inverso de " + f2 + "? = " + f1.esInverso(f2));

        System.out.println("\n--- INCISO e) PARSE ---");
        Fraccion f3 = Fraccion.parseFraccion("-2/3");
        System.out.println("parseFraccion(\"-2/3\") = " + f3);

        System.out.println("\n--- INCISO f) SIMPLIFICAR ---");
        Fraccion f4 = new Fraccion(2, 8);
        System.out.println(f4 + " simplificada = " + f4.simplifica());
    }
}