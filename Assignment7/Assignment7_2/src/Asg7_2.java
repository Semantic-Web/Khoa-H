import java.util.List;
import java.util.Scanner;

import org.geonames.ToponymSearchCriteria;
import org.geonames.ToponymSearchResult;
import org.geonames.WebService;
import org.geonames.PostalCode;




public class Asg7_2 
{

public static void main(String[] args) throws Exception 
	{
		System.out.println("******************* Searching for town/city and states *********************");
		System.out.println();
		System.out.println("Please go the this website to create an username if you don't have one:");
		System.out.println("****http://www.geonames.org/manageaccount**************");
		System.out.println();

		WebService.setUserName("khoafau");
				
		@SuppressWarnings("resource")
		Scanner reader = new Scanner(System.in);
			
		System.out.println("****************************************");
		System.out.println("Please enter fips code of a country that you want to search, for example: US, UK, DE, FR, CA, AS, JP, CN, IT,...");
		
		String searchInitial = reader.nextLine();

		System.out.println("***********************************************");
		
		System.out.println("You just entered " + (String) searchInitial );
		
		System.out.println("The Result of search ****************");
		ToponymSearchCriteria Initial = new ToponymSearchCriteria();
		Initial.setQ(searchInitial);
		ToponymSearchResult Result = null;
		Result = WebService.search(Initial);
		
		
		
		try {
			System.out.println("Number of searching: \t"+ Result.getTotalResultsCount());
			
			List<PostalCode> CountryCode1 = WebService.postalCodeSearch("", "",searchInitial);
									
			System.out.println("Number of printing records: "+ CountryCode1.size());
			System.out.println("******************");
						
													
			
			for (int i =0;i<CountryCode1.size();i++){
				
				System.out.println(i + "  City/town Name: \t"+ CountryCode1.get(i).getPlaceName());
				System.out.println("    State Name: \t"+ CountryCode1.get(i).getAdminName1());
				//System.out.println("Feature Code: \t"+ Result.getToponyms().get(i).getFeatureCode());//No Need
				
				System.out.println("   Latitude: \t"+ CountryCode1.get(i).getLatitude());
								
				System.out.println("   Longitude: \t"+ CountryCode1.get(i).getLongitude());
				
				System.out.println("   Zip Code Area: \t"+ CountryCode1.get(i).getPostalCode());
				
				System.out.println("   ISO-3166 alpha2: \t"+ CountryCode1.get(i).getCountryCode());
				
							
				
				System.out.println("********************************************");
				
				
			}
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
	}
	
}
