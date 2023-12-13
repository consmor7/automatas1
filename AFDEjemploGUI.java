import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class AFDEjemploGUI {
    private static JTable table;
    private static JButton verificarButton;
    private static JLabel resultadoLabel;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> createAndShowGUI());
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("AFD Ejemplo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        DefaultTableModel tableModel = new DefaultTableModel();
        table = new JTable(tableModel);
        tableModel.addColumn("Estado");
        tableModel.addColumn("0");
        tableModel.addColumn("1");

        tableModel.addRow(new String[] { "q0", "q1", "q0" });
        tableModel.addRow(new String[] { "q1", "q2", "q0" });
        tableModel.addRow(new String[] { "q2", "q2", "q2" });

        resultadoLabel = new JLabel();

        verificarButton = new JButton("Verificar Cadena");

        JPanel tablePanel = new JPanel(new BorderLayout());
        tablePanel.add(new JScrollPane(table), BorderLayout.CENTER);

        JPanel buttonPanel = new JPanel(new FlowLayout());
        buttonPanel.add(verificarButton);
        buttonPanel.add(resultadoLabel);

        JPanel mainPanel = new JPanel(new BorderLayout());
        mainPanel.add(tablePanel, BorderLayout.CENTER);
        mainPanel.add(buttonPanel, BorderLayout.SOUTH);

        frame.add(mainPanel);

        frame.setVisible(true);

        verificarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String cadenaAAnalizar = "110101}";
                boolean esAceptada = verificarCadena(cadenaAAnalizar);
                resultadoLabel.setText(esAceptada ? "Cadena aceptada" : "Cadena no aceptada");
            }
        });
    }

    public static boolean verificarCadena(String cadena) {
        DefaultTableModel tableModel = (DefaultTableModel) table.getModel();
        String estadoActual = "q0";
    
        for (char simbolo : cadena.toCharArray()) {
            int columna = simbolo == '0' ? 1 : simbolo == '1' ? 2 : -1;
            if (columna == -1) {
                return false; // Símbolo no válido
            }
    
            // Buscar el estado siguiente en la tabla
            Object estadoSiguiente = tableModel.getValueAt(buscarFila(estadoActual), columna);
            if (estadoSiguiente == null) {
                return false; // Transición no encontrada
            }
            
            estadoActual = estadoSiguiente.toString();
        }
    
        return estadoActual.equals("q0"); // Verificar si terminamos en q0 (estado de aceptación)
    }
    
    public static int buscarFila(String estado) {
        DefaultTableModel tableModel = (DefaultTableModel) table.getModel();
        for (int fila = 0; fila < tableModel.getRowCount(); fila++) {
            if (tableModel.getValueAt(fila, 0).toString().equals(estado)) {
                return fila;
            }
        }
        return -1; // Estado no encontrado
    }
}





