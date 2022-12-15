package com.example.app;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class Entradas extends AppCompatActivity {

    private RequestQueue queue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_entradas);
        queue = Volley.newRequestQueue(this);

        Button buttonFirst = (Button) findViewById(R.id.button_second);
        buttonFirst.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
                intent.setType("*/*");
                someActivityResultLauncher.launch(intent);
            }
        });
    }

    ActivityResultLauncher<Intent> someActivityResultLauncher = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            result -> {
                if (result.getResultCode() == Activity.RESULT_OK) {
                    Intent intent = result.getData();
                    Uri uri = intent.getData();
                    if (uri == null) return;
                    String csv = lerArquivo(uri);
                    if (csv == null) return;
                    enviarArquivo(csv);
                }
            });

    public String lerArquivo(Uri uri) {
        try {
            InputStream inputStream = getContentResolver().openInputStream(uri);
            StringBuilder textBuilder = new StringBuilder();
            try (Reader reader = new BufferedReader(new InputStreamReader
                    (inputStream, Charset.forName(StandardCharsets.UTF_8.name())))) {
                int c = 0;
                while ((c = reader.read()) != -1) {
                    textBuilder.append((char) c);
                }
            }
            String result = textBuilder.toString();
            inputStream.close();
            return result;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public void enviarArquivo(String csv) {
        JSONObject conteudo = new JSONObject();
        try {
            conteudo.put("csv", csv);
        } catch (JSONException e) {
            e.printStackTrace();
            return;
        }
        Activity contexto = this;

        JsonObjectRequest requisicao = new JsonObjectRequest(
                Request.Method.POST,
                "http://10.0.2.2:5000/",
                conteudo,
                response -> {
                    String json = response.toString();
                    contexto.runOnUiThread(() -> {
                        Intent resultado = new Intent(getApplicationContext(), Resultado.class);
                        resultado.putExtra("resultado", json);
                        startActivity(resultado);
                    });
                },
                error -> {
                    System.out.println("ERRO" + error.toString());
                }
        );

        queue.add(requisicao);
    }
}