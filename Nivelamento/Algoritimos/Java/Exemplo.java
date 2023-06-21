import java.util.Scanner;

public class Exemplo {

    public static void main(String[] args) {
        int idade1;
        // String nome;

        Scanner entrada = new Scanner(System.in);
        // Scanner entrada1 = new Scanner(System.in);

        System.out.println(
                "seja bem vindo ao curso de Java aqui vamos falar sobre a interação do Java na sociedade. Por gentileza, nos informe seu nome e a sua idade!");

        // System.out.println("Por favor, digite seu nome: ");
        // nome = entrada1.nextLine();

        System.out.println("Por favor, digite sua idade: ");
        idade1 = entrada.nextInt();
    }

}