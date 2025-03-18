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

@Controller
public class ImageController {

    private static final String UPLOAD_DIR = "uploads/";

    @GetMapping("/")
    public String index() {
        return "upload";
    }

    @PostMapping("/upload")
    public String handleFileUpload(@RequestParam("images") MultipartFile file, Model model) {
        try {
            // Save uploaded file
            String filename = UUID.randomUUID().toString() + "-" + file.getOriginalFilename();
            File uploadFile = new File(UPLOAD_DIR, filename);
            file.transferTo(uploadFile);

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
}
