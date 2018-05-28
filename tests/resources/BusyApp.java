// https://gist.github.com/sbilinski/24809966114a6b5089c2ada53eb0b4b7

public final class BusyApp {
  public static void main(String []args) throws Exception {
    final java.util.Random generator = new java.util.Random();
    while (true) {
      generator.ints(1000000, 0, 100).sorted();
      Thread.sleep(5000L);
    }
  }
}
