package com.example.app;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.util.Base64;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.gson.Gson;

public class Resultado extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_resultado);

        String json = getIntent().getStringExtra("resultado");
        if (json == null) finish();

        try {
            JsonResultado resultado = new Gson().fromJson(json, JsonResultado.class);
            byte[] base64 = Base64.decode(resultado.imagem, Base64.DEFAULT);
            Bitmap bitmap = BitmapFactory.decodeByteArray(base64, 0, base64.length);
            ((ImageView) findViewById(R.id.imageView10)).setImageBitmap(bitmap);

            ((TextView) findViewById(R.id.textView5)).setText("Accuracy = " + resultado.accuracy);
        } catch (Exception ex) {
            ex.printStackTrace();
            finish();
        }
    }
}