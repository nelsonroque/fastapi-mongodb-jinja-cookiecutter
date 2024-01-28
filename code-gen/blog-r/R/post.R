#' Create a new Post
#'
#' @description
#' Post Class
#'
#' @docType class
#' @title Post
#' @description Post Class
#' @format An \code{R6Class} generator object
#' @field created_utc  \link{AnyType} [optional]
#' @field title  \link{AnyType}
#' @field description  \link{AnyType}
#' @field body  \link{AnyType}
#' @field author_id  \link{AnyType}
#' @field slug  \link{AnyType}
#' @field tags  \link{AnyType}
#' @field published  \link{AnyType}
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
Post <- R6::R6Class(
  "Post",
  public = list(
    `created_utc` = NULL,
    `title` = NULL,
    `description` = NULL,
    `body` = NULL,
    `author_id` = NULL,
    `slug` = NULL,
    `tags` = NULL,
    `published` = NULL,
    #' Initialize a new Post class.
    #'
    #' @description
    #' Initialize a new Post class.
    #'
    #' @param title title
    #' @param description description
    #' @param body body
    #' @param author_id author_id
    #' @param slug slug
    #' @param tags tags
    #' @param published published
    #' @param created_utc created_utc
    #' @param ... Other optional arguments.
    #' @export
    initialize = function(`title`, `description`, `body`, `author_id`, `slug`, `tags`, `published`, `created_utc` = NULL, ...) {
      if (!missing(`title`)) {
        stopifnot(R6::is.R6(`title`))
        self$`title` <- `title`
      }
      if (!missing(`description`)) {
        stopifnot(R6::is.R6(`description`))
        self$`description` <- `description`
      }
      if (!missing(`body`)) {
        stopifnot(R6::is.R6(`body`))
        self$`body` <- `body`
      }
      if (!missing(`author_id`)) {
        stopifnot(R6::is.R6(`author_id`))
        self$`author_id` <- `author_id`
      }
      if (!missing(`slug`)) {
        stopifnot(R6::is.R6(`slug`))
        self$`slug` <- `slug`
      }
      if (!missing(`tags`)) {
        stopifnot(R6::is.R6(`tags`))
        self$`tags` <- `tags`
      }
      if (!missing(`published`)) {
        stopifnot(R6::is.R6(`published`))
        self$`published` <- `published`
      }
      if (!is.null(`created_utc`)) {
        stopifnot(R6::is.R6(`created_utc`))
        self$`created_utc` <- `created_utc`
      }
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return Post in JSON format
    #' @export
    toJSON = function() {
      PostObject <- list()
      if (!is.null(self$`created_utc`)) {
        PostObject[["created_utc"]] <-
          self$`created_utc`$toJSON()
      }
      if (!is.null(self$`title`)) {
        PostObject[["title"]] <-
          self$`title`$toJSON()
      }
      if (!is.null(self$`description`)) {
        PostObject[["description"]] <-
          self$`description`$toJSON()
      }
      if (!is.null(self$`body`)) {
        PostObject[["body"]] <-
          self$`body`$toJSON()
      }
      if (!is.null(self$`author_id`)) {
        PostObject[["author_id"]] <-
          self$`author_id`$toJSON()
      }
      if (!is.null(self$`slug`)) {
        PostObject[["slug"]] <-
          self$`slug`$toJSON()
      }
      if (!is.null(self$`tags`)) {
        PostObject[["tags"]] <-
          self$`tags`$toJSON()
      }
      if (!is.null(self$`published`)) {
        PostObject[["published"]] <-
          self$`published`$toJSON()
      }
      PostObject
    },
    #' Deserialize JSON string into an instance of Post
    #'
    #' @description
    #' Deserialize JSON string into an instance of Post
    #'
    #' @param input_json the JSON input
    #' @return the instance of Post
    #' @export
    fromJSON = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      if (!is.null(this_object$`created_utc`)) {
        `created_utc_object` <- AnyType$new()
        `created_utc_object`$fromJSON(jsonlite::toJSON(this_object$`created_utc`, auto_unbox = TRUE, digits = NA))
        self$`created_utc` <- `created_utc_object`
      }
      if (!is.null(this_object$`title`)) {
        `title_object` <- AnyType$new()
        `title_object`$fromJSON(jsonlite::toJSON(this_object$`title`, auto_unbox = TRUE, digits = NA))
        self$`title` <- `title_object`
      }
      if (!is.null(this_object$`description`)) {
        `description_object` <- AnyType$new()
        `description_object`$fromJSON(jsonlite::toJSON(this_object$`description`, auto_unbox = TRUE, digits = NA))
        self$`description` <- `description_object`
      }
      if (!is.null(this_object$`body`)) {
        `body_object` <- AnyType$new()
        `body_object`$fromJSON(jsonlite::toJSON(this_object$`body`, auto_unbox = TRUE, digits = NA))
        self$`body` <- `body_object`
      }
      if (!is.null(this_object$`author_id`)) {
        `author_id_object` <- AnyType$new()
        `author_id_object`$fromJSON(jsonlite::toJSON(this_object$`author_id`, auto_unbox = TRUE, digits = NA))
        self$`author_id` <- `author_id_object`
      }
      if (!is.null(this_object$`slug`)) {
        `slug_object` <- AnyType$new()
        `slug_object`$fromJSON(jsonlite::toJSON(this_object$`slug`, auto_unbox = TRUE, digits = NA))
        self$`slug` <- `slug_object`
      }
      if (!is.null(this_object$`tags`)) {
        `tags_object` <- AnyType$new()
        `tags_object`$fromJSON(jsonlite::toJSON(this_object$`tags`, auto_unbox = TRUE, digits = NA))
        self$`tags` <- `tags_object`
      }
      if (!is.null(this_object$`published`)) {
        `published_object` <- AnyType$new()
        `published_object`$fromJSON(jsonlite::toJSON(this_object$`published`, auto_unbox = TRUE, digits = NA))
        self$`published` <- `published_object`
      }
      self
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return Post in JSON format
    #' @export
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`created_utc`)) {
          sprintf(
          '"created_utc":
          %s
          ',
          jsonlite::toJSON(self$`created_utc`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`title`)) {
          sprintf(
          '"title":
          %s
          ',
          jsonlite::toJSON(self$`title`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`description`)) {
          sprintf(
          '"description":
          %s
          ',
          jsonlite::toJSON(self$`description`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`body`)) {
          sprintf(
          '"body":
          %s
          ',
          jsonlite::toJSON(self$`body`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`author_id`)) {
          sprintf(
          '"author_id":
          %s
          ',
          jsonlite::toJSON(self$`author_id`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`slug`)) {
          sprintf(
          '"slug":
          %s
          ',
          jsonlite::toJSON(self$`slug`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`tags`)) {
          sprintf(
          '"tags":
          %s
          ',
          jsonlite::toJSON(self$`tags`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`published`)) {
          sprintf(
          '"published":
          %s
          ',
          jsonlite::toJSON(self$`published`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        }
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      json_string <- as.character(jsonlite::minify(paste("{", jsoncontent, "}", sep = "")))
    },
    #' Deserialize JSON string into an instance of Post
    #'
    #' @description
    #' Deserialize JSON string into an instance of Post
    #'
    #' @param input_json the JSON input
    #' @return the instance of Post
    #' @export
    fromJSONString = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      self$`created_utc` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`created_utc`, auto_unbox = TRUE, digits = NA))
      self$`title` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`title`, auto_unbox = TRUE, digits = NA))
      self$`description` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`description`, auto_unbox = TRUE, digits = NA))
      self$`body` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`body`, auto_unbox = TRUE, digits = NA))
      self$`author_id` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`author_id`, auto_unbox = TRUE, digits = NA))
      self$`slug` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`slug`, auto_unbox = TRUE, digits = NA))
      self$`tags` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`tags`, auto_unbox = TRUE, digits = NA))
      self$`published` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`published`, auto_unbox = TRUE, digits = NA))
      self
    },
    #' Validate JSON input with respect to Post
    #'
    #' @description
    #' Validate JSON input with respect to Post and throw an exception if invalid
    #'
    #' @param input the JSON input
    #' @export
    validateJSON = function(input) {
      input_json <- jsonlite::fromJSON(input)
      # check the required field `title`
      if (!is.null(input_json$`title`)) {
        stopifnot(R6::is.R6(input_json$`title`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for Post: the required field `title` is missing."))
      }
      # check the required field `description`
      if (!is.null(input_json$`description`)) {
        stopifnot(R6::is.R6(input_json$`description`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for Post: the required field `description` is missing."))
      }
      # check the required field `body`
      if (!is.null(input_json$`body`)) {
        stopifnot(R6::is.R6(input_json$`body`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for Post: the required field `body` is missing."))
      }
      # check the required field `author_id`
      if (!is.null(input_json$`author_id`)) {
        stopifnot(R6::is.R6(input_json$`author_id`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for Post: the required field `author_id` is missing."))
      }
      # check the required field `slug`
      if (!is.null(input_json$`slug`)) {
        stopifnot(R6::is.R6(input_json$`slug`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for Post: the required field `slug` is missing."))
      }
      # check the required field `tags`
      if (!is.null(input_json$`tags`)) {
        stopifnot(R6::is.R6(input_json$`tags`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for Post: the required field `tags` is missing."))
      }
      # check the required field `published`
      if (!is.null(input_json$`published`)) {
        stopifnot(R6::is.R6(input_json$`published`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for Post: the required field `published` is missing."))
      }
    },
    #' To string (JSON format)
    #'
    #' @description
    #' To string (JSON format)
    #'
    #' @return String representation of Post
    #' @export
    toString = function() {
      self$toJSONString()
    },
    #' Return true if the values in all fields are valid.
    #'
    #' @description
    #' Return true if the values in all fields are valid.
    #'
    #' @return true if the values in all fields are valid.
    #' @export
    isValid = function() {
      TRUE
    },
    #' Return a list of invalid fields (if any).
    #'
    #' @description
    #' Return a list of invalid fields (if any).
    #'
    #' @return A list of invalid fields (if any).
    #' @export
    getInvalidFields = function() {
      invalid_fields <- list()
      invalid_fields
    },
    #' Print the object
    #'
    #' @description
    #' Print the object
    #'
    #' @export
    print = function() {
      print(jsonlite::prettify(self$toJSONString()))
      invisible(self)
    }
  ),
  # Lock the class to prevent modifications to the method or field
  lock_class = TRUE
)
## Uncomment below to unlock the class to allow modifications of the method or field
# Post$unlock()
#
## Below is an example to define the print function
# Post$set("public", "print", function(...) {
#   print(jsonlite::prettify(self$toJSONString()))
#   invisible(self)
# })
## Uncomment below to lock the class to prevent modifications to the method or field
# Post$lock()

