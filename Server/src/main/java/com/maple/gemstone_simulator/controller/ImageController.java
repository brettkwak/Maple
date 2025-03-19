package com.maple.gemstone_simulator.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
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
            @RequestParam("class") String className,
            @RequestParam("core_count") Integer coreCount,
            @RequestParam("image_count") Integer imageCount,
            // MultipartFile file, 
            Model model) {
        try {
            // Add all data to model
            logger.info("Setting flash attributes: dupCount={}, className={}, ...", dupCount, className);
            model.addAttribute("dupCount", dupCount);
            model.addAttribute("className", className); 
            model.addAttribute("coreCount", coreCount);
            model.addAttribute("imageCount", imageCount);


            // // Save uploaded file
            // String filename = UUID.randomUUID().toString() + "-" + file.getOriginalFilename();
            // File uploadFile = new File(UPLOAD_DIR, filename);
            // file.transferTo(uploadFile);

            return "results";
        } catch (Exception e) {
            e.printStackTrace();
            model.addAttribute("error", "Failed to process image.");
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
        return "results";
    }
}
