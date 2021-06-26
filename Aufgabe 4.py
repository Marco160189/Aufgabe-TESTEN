package de.marco160189.mockme;



public class Loh { // Lohnsteuer
  public CalcSteuer cs;

  public Loh(CalcSteuer thisCs) { // Konstruktor für Dependency Injection
    cs = thisCs;
  }
  
  public int calcBeitag(int brutto) {
    int netto = cs.calcNetto(brutto); // Analyse
    System.out.println("Nett XXX - Gehalt");
    return netto / 4; // Hoffentlich

public int add(int a2){
    return a2;
  }
public int div(int a2){
    return a2;
}

}
