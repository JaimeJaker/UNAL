import javax.swing.*;
import javax.swing.border.LineBorder;
import java.awt.*;
import java.io.*;


public class GestorContactos extends JFrame {
    private JTextField nameField, phoneField, emailField;
    private JTextArea outputArea;
    private Lista_Enlazada<Contacto> listaContactos;
    private ArbolBinarioBusqueda arbolContactos;
    private TablaHash tablaContactos;

    public GestorContactos() {
        setTitle("Gestor de Contactos Retro");
        setSize(500, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Inicializar estructuras de datos
        listaContactos = new Lista_Enlazada<>();
        arbolContactos = new ArbolBinarioBusqueda();
        tablaContactos = new TablaHash(10);

        // Cargar contactos desde el archivo
        cargarContactosDesdeArchivo();

        // Panel principal
        CustomPanel mainPanel = new CustomPanel();
        mainPanel.setLayout(null);

        // Etiquetas y campos de texto
        JLabel nameLabel = new JLabel("Nombre:");
        JLabel phoneLabel = new JLabel("Teléfono:");
        JLabel emailLabel = new JLabel("Email:");

        // Campos de texto
        nameField = new JTextField(15);
        phoneField = new JTextField(15);
        emailField = new JTextField(15);

        // Ubicar elementos en el panel
        nameLabel.setBounds(50, 60, 150, 20);
        nameField.setBounds(50, 80, 150, 25);
        phoneLabel.setBounds(50, 110, 150, 20);
        phoneField.setBounds(50, 130, 150, 25);
        emailLabel.setBounds(50, 160, 150, 20);
        emailField.setBounds(50, 180, 150, 25);

        // Agregar elementos al panel
        mainPanel.add(nameLabel);
        mainPanel.add(nameField);
        mainPanel.add(phoneLabel);
        mainPanel.add(phoneField);
        mainPanel.add(emailLabel);
        mainPanel.add(emailField);

        // Botones
        JButton addButton = new JButton("Agregar");
        JButton searchButton = new JButton("Buscar");
        JButton deleteButton = new JButton("Eliminar");
        JButton showButton = new JButton("Mostrar Todos");

        // Personalizar botones
        customizeButton(addButton);
        customizeButton(searchButton);
        customizeButton(deleteButton);
        customizeButton(showButton);

        addButton.setBounds(250, 80, 120, 30);
        searchButton.setBounds(250, 120, 120, 30);
        deleteButton.setBounds(250, 160, 120, 30);
        showButton.setBounds(250, 200, 120, 30);

        mainPanel.add(addButton);
        mainPanel.add(searchButton);
        mainPanel.add(deleteButton);
        mainPanel.add(showButton);

        // Eventos
        addButton.addActionListener(e -> addContact());
        searchButton.addActionListener(e -> searchContact());
        deleteButton.addActionListener(e -> deleteContact());
        showButton.addActionListener(e -> showAllContacts());

        // Área de salida
        outputArea = new JTextArea();
        outputArea.setEditable(false);
        outputArea.setBackground(new Color(230, 230, 250));
        outputArea.setBounds(50, 250, 320, 150);
        outputArea.setBorder(new LineBorder(Color.LIGHT_GRAY, 2));
        mainPanel.add(outputArea);

        add(mainPanel);
    }

    // Método para agregar contacto
    private void addContact() {
        String nombre = nameField.getText();
        String telefono = phoneField.getText();
        String email = emailField.getText();

        if (!nombre.isEmpty() && !telefono.isEmpty() && !email.isEmpty()) {
            Contacto nuevoContacto = new Contacto(nombre, telefono, email);

            listaContactos.insertar(nuevoContacto);
            arbolContactos.insertar(nuevoContacto);
            tablaContactos.insertar(nombre, nuevoContacto);

            outputArea.setText("Contacto agregado:\n" + nuevoContacto.toString());

            // Guardar los contactos en el archivo
            guardarContactosEnArchivo();
        } else {
            outputArea.setText("Por favor, complete todos los campos.");
        }

        nameField.setText("");
        phoneField.setText("");
        emailField.setText("");
    }

    // Método para eliminar contacto
    private void deleteContact() {
        String nombre = nameField.getText();
        if (!nombre.isEmpty()) {
            boolean eliminado = listaContactos.eliminar(nombre, c -> ((Contacto) c).nombre);
            if (eliminado) {
                tablaContactos.eliminar(nombre);
                outputArea.setText("Contacto eliminado: " + nombre);

                // Guardar los cambios en el archivo
                guardarContactosEnArchivo();
            } else {
                outputArea.setText("Contacto no encontrado: " + nombre);
            }
        } else {
            outputArea.setText("Ingrese el nombre del contacto a eliminar.");
        }
        nameField.setText("");
    }

    // Método para buscar contacto
    private void searchContact() {
        String nombre = nameField.getText();
        if (!nombre.isEmpty()) {
            Contacto encontrado = tablaContactos.buscar(nombre);
            if (encontrado != null) {
                outputArea.setText("Contacto encontrado:\n" + encontrado.toString());
            } else {
                outputArea.setText("Contacto no encontrado.");
            }
        } else {
            outputArea.setText("Ingrese el nombre del contacto a buscar.");
        }
        nameField.setText("");
    }

    // Método para mostrar todos los contactos
    private void showAllContacts() {
        if (!tablaContactos.estaVacia()) {
            StringBuilder contactos = new StringBuilder("Lista de contactos:\n");
            for (Contacto contacto : tablaContactos.obtenerTodos()) {
                contactos.append(contacto.toString()).append("\n");
            }
            outputArea.setText(contactos.toString());
        } else {
            outputArea.setText("No hay contactos para mostrar.");
        }
    }

    // Método para guardar los contactos en un archivo de texto
    public void guardarContactosEnArchivo() {
        try (PrintWriter writer = new PrintWriter(new FileWriter("contactos.txt"))) {
            for (Contacto contacto : tablaContactos.obtenerTodos()) {
                writer.println(contacto.nombre + "," + contacto.telefono + "," + contacto.email);
            }
        } catch (IOException e) {
            System.out.println("Error al guardar contactos: " + e.getMessage());
        }
    }

    // Método para cargar los contactos desde un archivo de texto
    public void cargarContactosDesdeArchivo() {
        try (BufferedReader reader = new BufferedReader(new FileReader("contactos.txt"))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                String[] partes = linea.split(",");
                String nombre = partes[0];
                String telefono = partes[1];
                String email = partes[2];

                Contacto contacto = new Contacto(nombre, telefono, email);
                listaContactos.insertar(contacto);
                arbolContactos.insertar(contacto);
                tablaContactos.insertar(nombre, contacto);
            }
        } catch (IOException e) {
            System.out.println("Error al cargar contactos: " + e.getMessage());
        }
    }

    private void customizeButton(JButton button) {
        button.setBackground(new Color(255, 182, 193));
        button.setForeground(Color.BLACK);
        button.setFocusPainted(false);
        button.setBorder(BorderFactory.createLineBorder(Color.BLACK, 2));
    }
    //hace toda la personalizacion del panel
    class CustomPanel extends JPanel {
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g;
            g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

            GradientPaint gradient = new GradientPaint(0, 0, new Color(173, 216, 230), 0, getHeight(), Color.WHITE);
            g2d.setPaint(gradient);
            g2d.fillRoundRect(10, 10, getWidth() - 20, getHeight() - 20, 30, 30);

            g2d.setColor(new Color(72, 209, 204));
            g2d.fillRoundRect(10, 10, getWidth() - 20, 40, 30, 30);

            g2d.setColor(Color.BLACK);
            g2d.setStroke(new BasicStroke(3));
            g2d.drawRoundRect(10, 10, getWidth() - 20, getHeight() - 20, 30, 30);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            GestorContactos window = new GestorContactos();
            window.setVisible(true);
        });
    }
}
