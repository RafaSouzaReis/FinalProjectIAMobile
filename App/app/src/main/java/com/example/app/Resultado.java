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

            ((TextView) findViewById(R.id.textView5)).setText("Accurancy = " + resultado.accurancy);
            ((TextView) findViewById(R.id.textView7)).setText("Precision = " + resultado.precision);
            ((TextView) findViewById(R.id.textView8)).setText("Recall = " + resultado.recall);
            ((TextView) findViewById(R.id.textView9)).setText("Specificity = " + resultado.specificity);
            ((TextView) findViewById(R.id.textView10)).setText("F1 Score = " + resultado.f1score);
            ((TextView) findViewById(R.id.textView11)).setText("Resultado Final = " + resultado.resultadofinal);
        } catch (Exception ex) {
            ex.printStackTrace();
            finish();
        }
    }
}