package com.maple.gemstone_simulator.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.UUID;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Controller
@RequestMapping("/")
@SessionAttributes({"dupCount", "className", "coreCount", "imageCount"})
public class ImageController {

    private static final Logger logger = LoggerFactory.getLogger(ImageController.class);

    private static final String UPLOAD_DIR = "uploads/";

    @GetMapping("/")
    public String index() {
        return "upload";
    }

    @PostMapping("/upload")
    public String handleFileUpload(
            @RequestParam("dup_count") Integer dupCount,
            @RequestParam("class_name") String className,
            @RequestParam("core_count") Integer coreCount,
            @RequestParam("image_count") Integer imageCount,
            RedirectAttributes redirectAttributes) {

        try {
            // Add all data to model

            
        
            logger.info("Setting flash attributes: dupCount={}, className={}, ...", dupCount, className);

            // Store data in flash attributes
            redirectAttributes.addFlashAttribute("dupCount", dupCount);
            redirectAttributes.addFlashAttribute("className", className);
            redirectAttributes.addFlashAttribute("coreCount", coreCount);
            redirectAttributes.addFlashAttribute("imageCount", imageCount);
        
            // Redirect to results page
            return "redirect:/results";
        } catch (Exception e) {
            e.printStackTrace();
            redirectAttributes.addAttribute("error", "Failed to process image.");
            return "upload";
        }
}

    @GetMapping("/images/{filename}")
    public ResponseEntity<Resource> serveFile(@PathVariable String filename) throws IOException {
        Path path = Paths.get(UPLOAD_DIR).resolve(filename);
        Resource resource = new UrlResource(path.toUri());
        return ResponseEntity.ok()
                .contentType(MediaType.IMAGE_JPEG)
                .body(resource);
    }

    @GetMapping("/results")
    public String showResults(Model model) {
        // You'll need to pass the same data to the model again here
        // This could be done by storing the data in session or retrieving it from a database
        logger.info("Model attributes after redirect: {}", model.asMap());
        return "results";
    }
}
