//using System.Diagnostics;
//using AutoDocumentTypeDetection.Models;
//using Microsoft.AspNetCore.Mvc;

//namespace AutoDocumentTypeDetection.Controllers
//{
//    public class HomeController : Controller
//    {
//        private readonly ILogger<HomeController> _logger;

//        public HomeController(ILogger<HomeController> logger)
//        {
//            _logger = logger;
//        }

//        public IActionResult Index()
//        {
//            return View();
//        }

//        public IActionResult Privacy()
//        {
//            return View();
//        }

//        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
//        public IActionResult Error()
//        {
//            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
//        }
//    }
//}
using Microsoft.AspNetCore.Mvc;
using System.Net.Http.Headers;
using DocumentAIWeb.Models;
using System.Text.Json;

public class HomeController : Controller
{
    private readonly HttpClient _client;

    public HomeController(IHttpClientFactory factory)
    {
        _client = factory.CreateClient();
    }

    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public async Task<IActionResult> Upload(IFormFile file)
    {
        var content = new MultipartFormDataContent();
        var fileContent = new StreamContent(file.OpenReadStream());
        fileContent.Headers.ContentType =
            new MediaTypeHeaderValue(file.ContentType);

        content.Add(fileContent, "file", file.FileName);

        var response = await _client.PostAsync(
            "http://127.0.0.1:8000/classify/", content);

        var json = await response.Content.ReadAsStringAsync();
        Console.WriteLine("========Response from FastAPI:=====");
        Console.WriteLine(json);

        //var result = JsonSerializer.Deserialize<ClassificationResponse>(
        //    json,
        //    new JsonSerializerOptions { PropertyNameCaseInsensitive = true });

        //ViewBag.Category = result.Category;
        //ViewBag.IsNew = result.Is_New_Type;

        //return View("Index");

            return Content(json, "application/json");
    }
}
