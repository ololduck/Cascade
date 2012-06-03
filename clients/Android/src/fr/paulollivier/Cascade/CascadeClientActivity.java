package fr.paulollivier.Cascade;

import android.app.Activity;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class CascadeClientActivity extends Activity {
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        Button savebutton = (Button) findViewById(R.id.savebutton);
        savebutton.setOnClickListener(new OnClickListener(){
        	public void onClick(View v){
        		// save preferences
        		Log.d("Preferences", "Getting shared prefs");
        		SharedPreferences sharedpref = getSharedPreferences("Cascade", Activity.MODE_PRIVATE);
        		Log.d("Preferences", "Getting editor...");
        		SharedPreferences.Editor editor = sharedpref.edit();
        		Log.d("Preferences", "Setting serv_addr...");
        		EditText et = (EditText) findViewById(R.id.et_serv_addr);
        		editor.putString("serv_addr", et.getText().toString());
        		et = null;
        		Log.d("Preferences", "Commiting..");
        		editor.commit();
        		Log.d("Preferences", "DONE");
        		Toast.makeText(getBaseContext(), R.string.saved_preferences_popup, Toast.LENGTH_LONG).show();
        	}
        });
    }
}