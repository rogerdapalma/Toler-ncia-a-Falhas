
import java.io.*;

public class FileExceptionHandling {
    public static void main(String[] args) {
        File file = new File("example.txt");
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(file));
            String line = null;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            throw new IOException("Simulated Error"); // Simula um erro durante a leitura
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO Error: " + e.getMessage());
        } finally {
            try {
                if (reader != null) {
                    reader.close();
                }
            } catch (IOException e) {
                System.out.println("Failed to close reader: " + e.getMessage());
            }
        }
    }
}
