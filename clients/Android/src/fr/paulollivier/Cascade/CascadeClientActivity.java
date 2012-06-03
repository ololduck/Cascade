package fr.paulollivier.Cascade;

import android.app.Activity;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
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
        		SharedPreferences sharedpref = getSharedPreferences("Cascade", Activity.MODE_PRIVATE);
        		SharedPreferences.Editor editor = sharedpref.edit();
        		editor.putString("serv_addr", (String) ((TextView) findViewById(R.id.et_serv_addr)).getText());
        		editor.commit();
        		Toast.makeText(getBaseContext(), R.string.saved_preferences_popup, Toast.LENGTH_LONG).show();
        	}
        });
    }
}