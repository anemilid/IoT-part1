package com.androidsrc.client;

import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends Activity {

	ImageView response;
	EditText editTextAddress, editTextPort,editTextAuthenticate;
	Button buttonConnect, buttonClear,buttonDisplay,buttonCancel,buttonOk;
	TextView detailsTextView;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);


		editTextAddress = (EditText) findViewById(R.id.addressEditText);
		editTextPort = (EditText) findViewById(R.id.portEditText);
		buttonConnect = (Button) findViewById(R.id.connectButton);
		buttonClear = (Button) findViewById(R.id.clearButton);
		response = (ImageView) findViewById(R.id.downloadView);
		buttonDisplay=(Button)findViewById(R.id.displayDetails);
		detailsTextView=(TextView)findViewById(R.id.detailsView);
		editTextAuthenticate=(EditText)findViewById(R.id.authenticateText);
		buttonCancel=(Button)findViewById(R.id.cancelButton);
		buttonOk=(Button)findViewById(R.id.okButton);

		detailsTextView.setVisibility(View.INVISIBLE);
		response.setVisibility(View.INVISIBLE);
		buttonDisplay.setVisibility(View.INVISIBLE);
		buttonCancel.setVisibility(View.INVISIBLE);
		buttonOk.setVisibility(View.INVISIBLE);
		editTextAuthenticate.setVisibility(View.INVISIBLE);

		buttonConnect.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View arg0) {
				Client myClient = new Client(editTextAddress.getText()
						.toString(), Integer.parseInt(editTextPort
						.getText().toString()), response,buttonDisplay);
				myClient.execute();
			}
		});

		buttonDisplay.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View arg0) {
				editTextAuthenticate.setVisibility(View.VISIBLE);
				buttonOk.setVisibility(View.VISIBLE);
				buttonCancel.setVisibility(View.VISIBLE);
				DisplayDetails myClient = new DisplayDetails(editTextAddress.getText()
						.toString(), Integer.parseInt(editTextPort
						.getText().toString()), detailsTextView);
				myClient.execute();
			}
		});


		buttonCancel.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View arg0) {
				uploadAuthenticationStatusToServer serverIpload=new uploadAuthenticationStatusToServer(editTextAddress.getText()
						.toString(), Integer.parseInt(editTextPort
						.getText().toString()),"cancelButton",buttonCancel,buttonOk,editTextAuthenticate);
				serverIpload.execute();

			}
		});

		buttonOk.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View arg0) {
				uploadAuthenticationStatusToServer serverIpload=new uploadAuthenticationStatusToServer(editTextAddress.getText()
						.toString(), Integer.parseInt(editTextPort
						.getText().toString()),"okButton",buttonCancel,buttonOk,editTextAuthenticate);
				serverIpload.execute();

			}
		});



		buttonClear.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				response.setImageAlpha(0);
				detailsTextView.setVisibility(View.INVISIBLE);
				editTextAuthenticate.setVisibility(View.INVISIBLE);
				buttonOk.setVisibility(View.INVISIBLE);
				buttonCancel.setVisibility(View.INVISIBLE);
				buttonDisplay.setVisibility(View.INVISIBLE);
			}
		});
	}

}
