package classes.com;

import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

import classes.com.Client;
import com.google.api.client.http.GenericUrl;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import classes.detecteur.Sonde;

public class Client_sonde extends Client{

	public Client_sonde() {
		super("http://localhost:5001/rest_api/v1.0/sonde");
	}

	@SuppressWarnings("unchecked")
	public List<Sonde> getsonde() {
			List<Sonde> listsonde=new ArrayList<Sonde>();
			request:try {
				request = requestFactory.buildGetRequest(new GenericUrl(getUrl()));
				String response = request.execute().parseAsString();
				if(response.isEmpty()) {
					break request;
				}				
				Type collectionType = new TypeToken<List<Sonde>>(){}.getType();
				listsonde = (List<Sonde>) new Gson()
				               .fromJson( response ,collectionType);
				} catch (IOException e) {
				e.printStackTrace();
			}
		return listsonde;
	}

	public void detection(int id) {
		try {

			request = requestFactory.buildGetRequest(new GenericUrl("http://localhost:5000/rest_api/v1.0/incendies/detection/"+String.valueOf(id)));
			String rawResponse = request.execute().parseAsString();
			System.out.println(rawResponse);
		}
		catch (IOException e) {
			e.printStackTrace();
		}
	}
}
