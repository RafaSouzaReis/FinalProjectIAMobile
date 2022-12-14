package com.example.app;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.fragment.NavHostFragment;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.util.ArrayList;

public class TelaPrincipal extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tela_principal);

        Button buttonFirst = (Button) findViewById(R.id.button_first);
        buttonFirst.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent membersIntent = new Intent(getApplicationContext(), Oque.class);
                startActivity(membersIntent);
            }
        });
        Button buttonTwo = (Button) findViewById(R.id.button_two);
        buttonTwo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent membersIntent = new Intent(getApplicationContext(), Integrantes.class);
                startActivity(membersIntent);
            }
        });
        Button buttonThree = (Button) findViewById(R.id.button_three);
        buttonThree.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent membersIntent = new Intent(getApplicationContext(), Entradas.class);
                startActivity(membersIntent);
            }
        });
    }
}