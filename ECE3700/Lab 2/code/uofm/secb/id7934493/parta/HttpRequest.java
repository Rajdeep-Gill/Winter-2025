package code.uofm.secb.id7934493.parta;

import java.io.*;
import java.net.*;

final class HttpRequest implements Runnable {

  final static String CRLF = "\r\n";
  Socket socket = null;

  // Constructor
  public HttpRequest(Socket socket) throws Exception {
    this.socket = socket;
  }

  // Implement the run() method of the Runnable interface
  public void run() {
    try {
      processRequest();
    } catch (Exception e) {
      System.out.println(e);
    }
  }

  // Does the actual processing of the request
  private void processRequest() throws Exception {
    // Get a reference to the socket's input and output streams
    InputStream is = socket.getInputStream();
    DataOutputStream os = new DataOutputStream(socket.getOutputStream());

    // Set up input stream filters
    InputStreamReader isr = new InputStreamReader(is);
    BufferedReader br = new BufferedReader(isr);

    // Get the request line of the HTTP request message
    String requestLine = br.readLine();

    // Display the request line
    System.out.println();
    System.out.println(requestLine);

    // Get and display the header lines
    String headerLine = null;
    while ((headerLine = br.readLine()).length() != 0) {
      System.out.println(headerLine);
    }

    // Create a basic response message
    String statusLine = "HTTP/1.1 200 OK" + CRLF;
    String contentTypeLine = "Content-Type: text/html" + CRLF;

    // Send the status line
    os.writeBytes(statusLine);
    // Send the content type line
    os.writeBytes(contentTypeLine);
    // Send a blank line to indicate the end of the header lines
    os.writeBytes(CRLF);

    os.close();
    br.close();
    socket.close();
  }

}
