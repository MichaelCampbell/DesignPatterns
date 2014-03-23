class Duck
	def initialize(string)
		@string = string
		puts "do something " + @string
	end

	def quack
		puts "Quaaaaaaack!"
	end

	def feathers
		puts "The duck has white and gray feathers."
	end
end

class Person
	def quack
		puts "The person imitates a duck"
	end

	def feathers
		puts "The person takes a feather from the ground and shows it."
	end
end

def in_the_forest(object)
	object.quack
	object.feathers
end

def game
	donald = Duck.new("duck")
	john = Person.new
	in_the_forest(donald)
	in_the_forest(john)
end

game